from googleapiclient import discovery
from functools import reduce
import pandas as pd

def getDisks(credential_object, project_id):
    service = discovery.build('compute', 'v1', credentials=credential_object)
    request = service.disks().aggregatedList(project=project_id)
    count = 1
    col = ['id', 'name', 'sizeGb', 'is_regional', 'region', 'zone', 
            'replica_zones', 'in_use', 'use_instance_name', 'creation_time']
    disk_df = pd.DataFrame(columns=col)
    disk_df = disk_df.astype({'is_regional':bool,'in_use':bool})

    while request is not None:
        response = request.execute()
        
        for name, disks_scoped_list in response['items'].items():
            if 'disks' in disks_scoped_list:
                for disk in disks_scoped_list['disks']:
                    is_regional, in_use = False, False
                    use_instance_name, region, zone, creationTime = '', '', '', ''
                    replica_zones = ''

                    id = disk['id']
                    name = disk['name']
                    sizeGb = disk['sizeGb']
                    if 'region' in disk:
                        is_regional = True
                        region = disk['region'].split('/')[-1]
                        replica_zones = [disk['replicaZones'][0].split('/')[-1], disk['replicaZones'][1].split('/')[-1]]
                        #['us-east1-b', 'us-east1-c']
                        replica_zones = reduce(lambda a, b : a+ " | " +str(b), replica_zones)
                    else:
                        zone = disk['zone'].split('/')[-1]

                    if 'users' in disk:
                        in_use = True
                        use_instance_name = disk['users'][0].split('/')[-1]
                    
                    if 'creationTimestamp' in disk:
                        creationTime = disk['creationTimestamp']

                    #print(count, id, name, sizeGb, is_regional, region, zone, replica_zones, in_use, use_instance_name, creationTime)
                    data_dict = {'id':id, 'name':name, 'sizeGb':sizeGb, 'is_regional':is_regional, 
                            'region':region, 'zone':zone, 'replica_zones':replica_zones, 'in_use':in_use, 
                            'use_instance_name':use_instance_name, 'creation_time':creationTime}
                    temp_df = pd.DataFrame(data_dict, index=[0])
                    disk_df = pd.concat([disk_df,temp_df])
                    count+=1
                

        request = service.disks().aggregatedList_next(previous_request=request, previous_response=response)
    return disk_df