from googleapiclient import discovery

def getDisks(credential_object, project_id):
    service = discovery.build('compute', 'v1', credentials=credential_object)
    request = service.disks().aggregatedList(project=project_id)
    while request is not None:
        response = request.execute()
        
        for name, disks_scoped_list in response['items'].items():
            # TODO: Change code below to process each (name, disks_scoped_list) item:
            print(disks_scoped_list)

        request = service.disks().aggregatedList_next(previous_request=request, previous_response=response)