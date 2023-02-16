import Authentication
import DiskUsage
import GetInstances
import SnapUsage
import IpUsage
import BucketUsage
import pandas as pd

project_id = 'vsa-dev-298916'
json_key_location = 'C:/Users/hmalik/Documents/vsa-dev-298916-7a558f236b34.json'


credential_object = Authentication.getAuth(json_key_location)

ips = IpUsage.getStaticIP(credential_object, project_id)

disks = DiskUsage.getDisks(credential_object, project_id)

instances = GetInstances.getInstances(credentials=credential_object,
                          project_id=project_id)


buckets = BucketUsage.getBuckets(credential_object, project_id)


snaps = SnapUsage.getSnaps(credential_object=credential_object,
                   project_id=project_id)
with pd.ExcelWriter("test.xlsx") as writer:
    instances.to_excel(writer, sheet_name="instances", index=False)
    disks.to_excel(writer, sheet_name="disks", index=False) 
    buckets.to_excel(writer, sheet_name="buckets",index=False)
    ips.to_excel(writer, sheet_name="IPs",index=False)
    snaps.to_excel(writer, sheet_name="Snapshots", index=False)
