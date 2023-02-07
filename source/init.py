import Authentication
import DiskUsage

project_id = 'vsa-dev-298916'
json_key_location = '/Users/abiswas/Desktop/LOGS/IAM_JSON/vsa-dev-298916-7a558f236b34.json'


credential_object = Authentication.getAuth(json_key_location)

DiskUsage.getDisks(credential_object, project_id)