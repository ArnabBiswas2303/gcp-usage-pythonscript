import Authentication
import DiskUsage
import GetInstances
import SnapUsage

project_id = 'vsa-dev-298916'
json_key_location = 'C:/Users/hmalik/Documents/vsa-dev-298916-7a558f236b34.json'


credential_object = Authentication.getAuth(json_key_location)

DiskUsage.getDisks(credential_object, project_id)

GetInstances.getInstances(credentials=credential_object,
                          project_id='vsa-dev-298916')

SnapUsage.getSnaps(credential_object=credential_object,
                   project_id=project_id)
