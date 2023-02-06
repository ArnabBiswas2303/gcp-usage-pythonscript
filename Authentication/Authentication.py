from google.oauth2 import service_account
from googleapiclient import discovery
from google.cloud import storage as dns
import json

project_id = 'vsa-dev-298916'


gcp_service_account_json = None
with open("/Users/tjaiswal/Downloads/vsa-dev-298916-7a558f236b34.json") as json_file:
    gcp_service_account_json = json.load(json_file)

credentials = service_account.Credentials.from_service_account_info(
    gcp_service_account_json)


client = dns.Client(project=project_id, credentials=credentials)
