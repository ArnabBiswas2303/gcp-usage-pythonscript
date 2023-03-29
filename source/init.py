import Authentication
import DiskUsage
import GetInstances
import SnapUsage
import IpUsage
import BucketUsage
import GetKeys
import Email
import pandas as pd
import datetime as DT
import numpy as np
import os
from googleapiclient import discovery

json_key_location = str(os.getenv('GCP_SCRIPT_JSON_KEY_PATH'))


def GetUsage(project_id):
    actionable_items = {}
    today = DT.datetime.now().strftime("%d %b, %Y")
    week_ago = (DT.datetime.now() - DT.timedelta(days=6)).strftime("%d %b, %Y")
    date_condition = pd.date_range(start=week_ago, end=today, inclusive='both')
    date_condition = [i.strftime("%Y-%m-%d") for i in date_condition]
    credential_object = Authentication.getAuth(json_key_location)

    # fetch ips usage
    ips = IpUsage.getStaticIP(credential_object, project_id)
    ips = ips.reset_index(drop=True)
    highlighted_rows_ips = np.where(ips['creation_time'].isin(date_condition),
                                    'background-color: yellow',
                                    '')
    ip_styler = ips.style.apply(lambda _: highlighted_rows_ips)

    # fetch disk usage
    disks = DiskUsage.getDisks(credential_object, project_id)
    disks = disks.reset_index(drop=True)
    highlighted_rows_disks = np.where(disks['creation_time'].isin(date_condition),
                                    'background-color: yellow',
                                    '')
    disk_styler = disks.style.apply(lambda _: highlighted_rows_disks)
    actionable_disks = pd.DataFrame()
    actionable_disks = disks.loc[disks['sizeGb'].astype(int)>=200]
    actionable_disks = actionable_disks[['name','sizeGb']] if actionable_disks.shape[0] else actionable_disks
    if not actionable_disks.empty:
        action_disks = []
        for name, sizeGb in actionable_disks.iloc[:,:].to_numpy():
            d = {}
            d['diskName'] = name
            d['diskSize'] = sizeGb
            action_disks.append(d)
        actionable_disks['disks'] = action_disks

    # fetch instance usage
    instances = GetInstances.getInstances(credentials=credential_object,
                                        project_id=project_id)
    instances = instances.reset_index(drop=True)
    highlighted_rows_instances = np.where(instances['creation_time'].isin(date_condition),
                                        'background-color: yellow',
                                        '')
    highlighted_rows_instances = np.where(instances['nodeGroupName'].isna(
    ), highlighted_rows_instances, 'background-color: red')
    instances_styler = instances.style.apply(lambda _: highlighted_rows_instances)
    actionable_instances = pd.DataFrame()
    actionable_instances = instances.loc[~instances['nodeGroupName'].isna()]
    actionable_instances = actionable_instances[['name',' nodeGroupName','nodeName']] if actionable_instances.shape[0] else actionable_instances
    if not actionable_instances.empty:
        sole_tenants = []
        for name,nodeGroupName, nodeName in actionable_disks.iloc[:,:].to_numpy():
            sole_tenant = {}
            sole_tenant['instance_name'] = name
            sole_tenant['nodeAffinity'] = nodeGroupName + '|' + str(nodeName)
            sole_tenants.append(sole_tenant)
        actionable_items['instances'] = sole_tenants


    # fetch bucket usage
    buckets = BucketUsage.getBuckets(credential_object, project_id)
    buckets = buckets.reset_index(drop=True)
    highlighted_rows_buckets = np.where(buckets['creation_time'].isin(date_condition),
                                        'background-color: yellow',
                                        '')
    buckets_styler = buckets.style.apply(lambda _: highlighted_rows_buckets)


    # fetch keys details
    keys = GetKeys.getKeys(credentials=credential_object, projectId=project_id)

    # fetch snap usage
    snaps = SnapUsage.getSnaps(credential_object=credential_object,
                            project_id=project_id)
    snaps = snaps.reset_index(drop=True)
    highlighted_rows_snaps = np.where(snaps['creation_time'].isin(date_condition),
                                    'background-color: yellow',
                                    '')
    snaps_styler = snaps.style.apply(lambda _: highlighted_rows_snaps)
    actionable_snaps = pd.DataFrame()
    actionable_snaps = snaps.loc[snaps['source_disk_size'].astype(int)>200]
    actionable_snaps = actionable_snaps['snap_name','source_disk_size'] if actionable_snaps.shape[0] else actionable_snaps
    if not actionable_snaps.empty:
        action_snaps = []
        for snap_name,source_disk_size in actionable_snaps.iloc[:,:].to_numpy():
            action_snap = {}
            action_snap['snapshotName'] = snap_name
            action_snap['snapshotSize'] = source_disk_size
            sole_tenants.append(action_snap)
        actionable_items['snapshots'] = action_snaps

    

    with pd.ExcelWriter("{0}.xlsx".format(project_id)) as writer:
        if instances.shape[0] != 0:
            instances_styler.to_excel(writer, sheet_name="instances", index=False)

        if disks.shape[0] != 0:
            disk_styler.to_excel(writer, sheet_name="disks", index=False)

        if buckets.shape[0] != 0:
            buckets_styler.to_excel(writer, sheet_name="buckets", index=False)

        if ips.shape[0] != 0:
            ip_styler.to_excel(writer, sheet_name="IPs", index=False)

        if snaps.shape[0] != 0:
            snaps_styler.to_excel(writer, sheet_name="Snapshots", index=False)

        if keys.shape[0] != 0:
            keys.to_excel(writer, sheet_name="Keys", index=False)

    return len(instances), len(disks), len(snaps), len(buckets), len(ips), len(keys), {project_id:actionable_items}


total_instances = total_disks = total_snaps = total_bukets = total_ips = total_keys = 0
total_projects = []


# Get All Projects
project_ids = []
credential_object = Authentication.getAuth(json_key_location)
service = discovery.build('cloudresourcemanager', 'v1', credentials=credential_object)
request = service.projects().list()
while request is not None:
    response = request.execute()
    projects = response['projects']
    for project in projects:
        project_ids.append(project['projectId'])
    request = service.projects().list_next(previous_request=request, previous_response=response)
print(project_ids)

for project_id in project_ids:
    instances, disks, snaps, buckets, ips, keys, actionable_items = GetUsage(project_id)
    print('actionable items--')
    print(actionable_items)
    print()
    proj_obj = {
        "project_id": project_id,
        "instances": instances,
        "disks": disks,
        "snapshots": snaps
    }

    total_projects.append(proj_obj)
    total_instances += instances
    total_disks += disks
    total_snaps += snaps
    total_bukets += buckets
    total_ips += ips
    total_keys += keys

Email.sendMail(total_instances, total_disks, total_snaps, total_projects)
