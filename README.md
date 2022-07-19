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

First, we simply load the PyDaisi package:

```python
import pydaisi as pyd
```

Next, we connect to the Daisi:

```python
twitter_search = pyd.Daisi("erichare/Twitter Search")
```

Next, let's provide a query to search Twitter with:

```python
twitter_search.fetch_tweets(query="Daisi", count=10).value
```

And that's it! We have a clean dataframe containing the author of the tweet and the text of the tweet based on the query!
