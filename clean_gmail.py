from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://mail.google.com/"]


def get_service():
    """
    Returns Gmail API service resource
    """
    flow = InstalledAppFlow.from_client_secrets_file(f"./client_secret.json", SCOPES)
    creds = flow.run_local_server(
        port=0, access_type="offline", prompt="consent", include_granted_scopes=False
    )
    return build("gmail", "v1", credentials=creds)


def list_labels(service):
    """
    Util to list available labels
    """
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])
    for label in labels:
        print(f"{label['name']} (ID: {label['id']})")


def construct_query(category: str, exclude_labels: list[str] = []):
    """
    Construct Gmail API filter query
    """
    query = f"category:{category}"
    if len(exclude_labels):
        for label in exclude_labels:
            query += f" -label:{label}"
    return query


def delete_category(service, category: str, query: str):
    """
    Delete emails by category. Modify logic as and when needed
    """
    page_token = None
    total_count = 0
    while True:
        results = (
            service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=1000,
                pageToken=page_token,
            )
            .execute()
        )
        messages = results.get("messages", [])
        if not messages:
            print(f"No more emails in {category} ")
            break

        ids = [msg["id"] for msg in messages]
        service.users().messages().batchDelete(userId="me", body={"ids": ids}).execute()
        print(f"Deleted {len(ids)} emails from {category})...")
        total_count += len(ids)

        page_token = results.get("nextPageToken")
        if not page_token:
            break

    print(f"Total deleted: {total_count}")


def main():
    category = "updates"
    service = get_service()
    exclude_labels = [  # Provide as needed
        "max-life-insurance",
        "mutual-funds",
        "github",
        "aws",
        "tricog",
        "whyminds",
        "tcs",
    ]
    delete_category(service, "updates", construct_query(category, exclude_labels))
    # list_labels(service)


if __name__ == "__main__":
    main()
