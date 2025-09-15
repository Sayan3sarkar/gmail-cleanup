# Clear Gmail Inbox Utility

A simple util function to help clear gmail inbox by category. The idea I applied was to have my important emails labelled, so that I could exclude them from the query to be fed to the gmail API. Customise to your needs

## Secrets Encryption and decrytion

<b>NOTE:</b> Make sure to not forget your passphrase(set during encryption) - or else this key can't be recovered

### secret_key encryption

```bash
openssl enc -aes-256-cbc -md sha512 -pbkdf2 -iter 10000 -salt -in client_secret.json -out encrypted_client_secret.txt -e
```

### secret key decryption

```bash
openssl enc -aes-256-cbc -md sha512 -pbkdf2 -in encrypted_client_secret.txt -out client_secret.json -d
```

## GCP secret key generation steps

- Visit [google cloud console](https://console.cloud.google.com)
- Create a project (name it appropriately) and select that project so that you're inside it
- Go to `APIs and Services` -> `Enabled APIs and services` -> Search for `Gmail API` -> Select it -> `Enable`
- Go to `Credentials` tab -> `Create Credentials` -> Select `Oauth client Id`
- Select `Application Type` = `Desktop App` -> set an apt name -> `Create`
- You will see `Oauth client created` popup
- <b>DOWNLOAD and SECURELY STORE the json</b> by hitting `Download JSON`
- Rename Downloaded file to `client_secret.json` and put it inside this directory
- Proceed with the encryption/decryption as needed (and stated above)
- Under `Credentials`, go to `OAuth 2.0 client Ids` -> Select your client
- On the left nav bar, go to `Data Access` -> `Add or remove scopes`
- In the search bar which appears with list of scopes, search for `Gmail API` -> List of all scopes associated appear -> Select all just to be on the safe side -> Hit `Update`
- It may ask for verification, but you can skip it. you just have to make sure to add your email as a test user. Refer to this: https://developers.google.com/workspace/guides/configure-oauth-consent

## Installation

Create venv, if needed. Install requirements as follows

```bash
pip install -r requirements.txt
```

## Startup

```bash
python3 clean_gmail.py
```
