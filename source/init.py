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
ips = ips.reset_index(drop=True)
highlighted_rows = np.where(ips['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
ip_styler = ips.style.apply(lambda _: highlighted_rows)

#fetch disk usage
disks = DiskUsage.getDisks(credential_object, project_id)
disks = disks.reset_index(drop=True)
highlighted_rows = np.where(disks['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
disk_styler = disks.style.apply(lambda _: highlighted_rows)

#fetch instance usage
instances = GetInstances.getInstances(credentials=credential_object,
                          project_id=project_id)
instances = instances.reset_index(drop=True)
highlighted_rows_instances = np.where(instances['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
instances_styler = instances.style.apply(lambda _: highlighted_rows_instances)

# #fetch bucket usage
# buckets = BucketUsage.getBuckets(credential_object, project_id)
# buckets = buckets.reset_index(drop=True)
# highlighted_rows = np.where(buckets['creation_time'].isin(date_condition),
#                             'background-color: yellow',
#                             '')
# buckets_styler = buckets.style.apply(lambda _: highlighted_rows)


#fetch snap usage
snaps = SnapUsage.getSnaps(credential_object=credential_object,
                   project_id=project_id)
snaps = snaps.reset_index(drop=True)
highlighted_rows = np.where(snaps['creation_time'].isin(date_condition),
                            'background-color: yellow',
                            '')
snaps_styler = snaps.style.apply(lambda _: highlighted_rows)


with pd.ExcelWriter("test.xlsx") as writer:
    instances_styler.to_excel(writer, sheet_name="instances", index=False)
    disk_styler.to_excel(writer, sheet_name="disks", index=False) 
    # #buckets_styler.to_excel(writer, sheet_name="buckets",index=False)
    ip_styler.to_excel(writer, sheet_name="IPs",index=False)
    snaps_styler.to_excel(writer, sheet_name="Snapshots", index=False)

