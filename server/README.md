# Server Folder 
(Keeper: 민거홍, @placidmoon1)

## Server Address:
https://milidoc.web.app

## Supported HTTP Requests:
- GET **/**


## HowTo (MAC/Linux Only)
0. [After writing your code, freeze all required modules using 
`pip3 freeze > requirements.txt`]

### Flask Setup

1. Create your `venv` at the root folder using 
`$ . venv/bin/activate` (MAC/Linux Only)

2. Install all requirements for this project using `pip3 install -r requirements.txt` at root.

3. Create a `secrets.py` folder in `server/src`. **THIS FILE MUST NOT BE UPLOADED IN A PUBLIC REPO!**     

    Include:

    (1) A `firebaseConfig` JSON variable containing at least `apiKey`, `authDomain`, `databaseURL`, and `storageBucket` from Firebase.

    (2) A `app_secret_key` variable with a string value of a complicated hexadecimal key

    Indicate in top-level `.gitignore` to ignore this file, by including `server/src/secrets.py`

### [GCP Setup]

