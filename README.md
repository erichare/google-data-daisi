# Google Data Studio Storage with Daisies

## Prerequisites

First, you must have a service account created. Please follow the very useful guide from [PracticalDataScience](https://practicaldatascience.co.uk/data-engineering/how-to-create-a-google-service-account-client-secrets-json-key).

In the Google Developers Console:

1. Go to the Google Developers Console
2. Ensure you are logged in to the correct Google account
3. Search for the API service you wish to enable, the "Google Drive API", and click "Enable"
4. Go to APIs and Services > Credentials and click “+ Create Credentials” and select “Service Account”
5. Enter a name for the service account, i.e. “Google Search Console API service account”.
6. Change the email to something you’ll recognise, i.e. “gsc-api-service-account@”.
7. Click “Create and Continue” and select a role, i.e. Basic > Viewer, then click “Done”.
8. Copy the email address created, i.e. gsc-api-service-account@xxxxxxxxxxx.iam.gserviceaccount.com
9. In Credentials > Service Accounts click the email address added
10. Click “Keys” > “Add key” > “Create new key” > “JSON” > “Create”
11. Download the key and give it a name to identify what it does, i.e. mysite-client-secrets.json

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
