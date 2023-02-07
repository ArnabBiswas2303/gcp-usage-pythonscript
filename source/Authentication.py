import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account
import json

def getAuth(projectId, jsonKeyLocation):    
    gcp_service_account_json = None
    with open(jsonKeyLocation) as json_file:
        gcp_service_account_json = json.load(json_file)

    credentials = service_account.Credentials.from_service_account_info(
        gcp_service_account_json, scopes=['https://www.googleapis.com/auth/cloud-platform'])
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    # print(credentials.token) -> Prints the token
    return credentials
