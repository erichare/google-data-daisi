# Google Spreadsheets with Daisies

## Prerequisites

To use this Daisi, you must first have a service account created for your Google Account with the Google Drive API enabled. Please use the following steps to create this service account:

In the [Google Developers Console](https://console.cloud.google.com/apis/dashboard):

1. Ensure you are logged in to the correct Google account
2. Search for the API service you wish to enable, the "Google Drive API", and click "Enable"
3. Go to APIs and Services > Credentials and click “+ Create Credentials” and select “Service Account”
4. Enter a name for the service account, i.e. “Google Drive Service Account”.
5. Change the email to something you’ll recognize, i.e. “gd-api-service-account@gmail.com”.
6. Click “Create and Continue” and select a role, i.e. Basic > Viewer, then click “Done”.
7. Copy the email address created, i.e. gsc-api-service-account@xxxxxxxxxxx.iam.gserviceaccount.com
8. In Credentials > Service Accounts click the email address added
9. Click “Keys” > “Add key” > “Create new key” > “JSON” > “Create”
10. Download the key and give it a name to identify what it does, i.e. mysite-client-secrets.json

## How to Call

After generating your JSON Service Account key per the above instructions, we simply load the PyDaisi package:

```python
import pydaisi as pyd
```

Next, we connect to the Daisi:

```python
gds = pyd.Daisi("erichare/Google Data Studio")
```

Then, we call the Daisi:

```python
gds.store_in_gs(df, email, service_account).value
```

Passing in the values of `df`, `email`, and `service_account` as a path to your service account JSON.
