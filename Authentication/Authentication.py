import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account
from google.oauth2 import service_account
from googleapiclient import discovery
from google.cloud import storage as dns
import json

project_id = 'vsa-dev-298916'


gcp_service_account_json = None
with open("/Users/tanmaygarg/Downloads/Account.json") as json_file:
    gcp_service_account_json = json.load(json_file)

credentials = service_account.Credentials.from_service_account_info(
    gcp_service_account_json, scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)
# print(credentials.token)
