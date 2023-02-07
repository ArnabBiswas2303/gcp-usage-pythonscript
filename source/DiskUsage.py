from googleapiclient import discovery

def getDisks(credential_object, project_id):
    service = discovery.build('compute', 'v1', credentials=credential_object)
    request = service.disks().aggregatedList(project=project_id)
    while request is not None:
        response = request.execute()
        
        for name, disks_scoped_list in response['items'].items():
            if 'disks' in disks_scoped_list:
                for disk in disks_scoped_list['disks']:
                    is_regional, in_use = False, False
                    use_instance_name, region, zone = '', '', ''
                    replica_zones = []

                    id = disk['id']
                    name = disk['name']
                    sizeGb = disk['sizeGb']

                    if 'region' in disk:
                        is_regional = True
                        region = disk['region'].split('/')[-1]
                        replica_zones = [disk['replicaZones'][0].split('/')[-1], disk['replicaZones'][1].split('/')[-1]]
                    else:
                        zone = disk['zone'].split('/')[-1]

                    if 'users' in disk:
                        in_use = True
                        use_instance_name = disk['users'][0].split('/')[-1]

                    print(id, name, sizeGb, is_regional, region, zone, replica_zones, in_use, use_instance_name)
                

        request = service.disks().aggregatedList_next(previous_request=request, previous_response=response)