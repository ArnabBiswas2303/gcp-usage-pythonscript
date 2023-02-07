from googleapiclient import discovery


def getInstances(credentials, project_id):

    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().aggregatedList(project=project_id)
    while request is not None:
        response = request.execute()
        for zone in response['items']:
            if 'instances' in response['items'][zone]:
                for instance in response['items'][zone]['instances']:
                    print(instance['name'], instance['id'],
                          len(instance['disks']), end=' ')
                    for disk in instance['disks']:
                        if disk['boot'] == True:
                            print(disk['licenses'][0].split('/')[-1])

        request = service.instances().aggregatedList_next(
            previous_request=request, previous_response=response)
