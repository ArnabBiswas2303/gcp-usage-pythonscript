import Authentication
import DiskUsage
import GetInstances
import SnapUsage
import IpUsage
import BucketUsage
import GetKeys
import pandas as pd

project_id = 'vsa-dev-298916'
json_key_location = 'C:/Users/tjaiswal/Downloads/Account.json'


credential_object = Authentication.getAuth(json_key_location)

ips = IpUsage.getStaticIP(credential_object, project_id)

disks = DiskUsage.getDisks(credential_object, project_id)

instances = GetInstances.getInstances(credentials=credential_object,
                                      project_id=project_id)


buckets = BucketUsage.getBuckets(credential_object, project_id)


snaps = SnapUsage.getSnaps(credential_object=credential_object,
                           project_id=project_id)

keys = GetKeys.getKeys(credentials=credential_object, projectId=project_id)

with pd.ExcelWriter("GCP-USAGE.xlsx") as writer:
    if instances.shape[0] != 0:
        instances.to_excel(writer, sheet_name="instances", index=False)

    if disks.shape[0] != 0:
        disks.to_excel(writer, sheet_name="disks", index=False)

    if buckets.shape[0] != 0:
        buckets.to_excel(writer, sheet_name="buckets", index=False)

    if ips.shape[0] != 0:
        ips.to_excel(writer, sheet_name="IPs", index=False)

    if snaps.shape[0] != 0:
        snaps.to_excel(writer, sheet_name="Snapshots", index=False)

    if keys.shape[0] != 0:
        keys.to_excel(writer, sheet_name="Keys", index=False)
