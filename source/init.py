import Authentication
import DiskUsage
import GetInstances
import SnapUsage
import IpUsage
import BucketUsage
import pandas as pd
import datetime as DT
import numpy as np

project_id = 'vsa-dev-298916'
json_key_location = 'C:/Users/hmalik/Documents/vsa-dev-298916-7a558f236b34.json'

today = DT.datetime.now().strftime("%d %b, %Y")
week_ago = (DT.datetime.now() - DT.timedelta(days = 6)).strftime("%d %b, %Y")
date_condition = pd.date_range(start = week_ago, end = today, inclusive='both')
date_condition = [i.strftime("%Y-%m-%d") for i in date_condition]
credential_object = Authentication.getAuth(json_key_location)

#fetch ips usage
ips = IpUsage.getStaticIP(credential_object, project_id)
highlighted_rows = np.where(ips['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
ips = ips.style.apply(lambda _: highlighted_rows)

disks = DiskUsage.getDisks(credential_object, project_id)

#fetch instance usage
instances = GetInstances.getInstances(credentials=credential_object,
                          project_id=project_id)
highlighted_rows = np.where(instances['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
instances = instances.style.apply(lambda _: highlighted_rows)
#print(instances)

#fetch bucket usage
buckets = BucketUsage.getBuckets(credential_object, project_id)
highlighted_rows = buckets['creation_time'].isin(date_condition).map({
    True: 'background-color: yellow',
    False: ''
})
buckets = buckets.style.apply(lambda _: highlighted_rows)

#fetch snap usage
snaps = SnapUsage.getSnaps(credential_object=credential_object,
                   project_id=project_id)
highlighted_rows = np.where(snaps['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
snaps = snaps.style.apply(lambda _: highlighted_rows)

with pd.ExcelWriter("test.xlsx") as writer:
    instances.to_excel(writer, sheet_name="instances", index=False)
    disks.to_excel(writer, sheet_name="disks", index=False) 
    buckets.to_excel(writer, sheet_name="buckets",index=False)
    ips.to_excel(writer, sheet_name="IPs",index=False)
    snaps.to_excel(writer, sheet_name="Snapshots", index=False)
