import Authentication
import DiskUsage
import GetInstances

project_id = 'vsa-dev-298916'
json_key_location = '/Users/tjaiswal/Downloads/Account.json'


credential_object = Authentication.getAuth(json_key_location)

DiskUsage.getDisks(credential_object, project_id)

GetInstances.getInstances(credentials=credential_object,
                          project_id='vsa-dev-298916')
