from googleapiclient import discovery
from datetime import datetime
import pandas as pd

# constants
nodeGroupNameKey = 'compute.googleapis.com/node-group-name'
nodeNameKey = 'compute.googleapis.com/node-name'


def getInstances(credentials, project_id):

    service = discovery.build('compute', 'v1', credentials=credentials)
    request = service.instances().aggregatedList(project=project_id)

    counter = 1
    col = ['instanceName', 'instanceId', 'creation_time', 'diskCount',
                        'guestOS', 'natIP', 'nodeGroupName', 'nodeName']
    instance_df = pd.DataFrame(columns=col)
    while request is not None:
        response = request.execute()
        for zone in response['items']:
            if 'instances' in response['items'][zone]:
                for instance in response['items'][zone]['instances']:
                    instanceName, instanceId, diskCount = instance['name'], instance['id'], len(
                        instance['disks'])
                    natIP, guestOS, creation_time = None, None, None
                    nodeGroupName, nodeName = None, None

                    if 'creationTimestamp' in instance:
                        creation_time = instance['creationTimestamp'].split('T')[0]
                        UTCTime = datetime.strptime(creation_time, "%Y-%m-%d")
                        epochTime = (UTCTime - datetime(1970, 1, 1)
                                     ).total_seconds()
                        timeObj = datetime.fromtimestamp(epochTime)
                        creation_time = timeObj.strftime("%Y-%m-%d")

                    if 'networkInterfaces' in instance and 'accessConfigs' in instance['networkInterfaces'][0]:
                        accessConfigs = instance["networkInterfaces"][0]['accessConfigs'][0]
                        natIP = accessConfigs['natIP'] if 'natIP' in accessConfigs else None

                    for disk in instance['disks']:
                        if disk['boot'] == True:
                            guestOS = disk['licenses'][0].split('/')[-1]

                    if 'nodeAffinities' in instance['scheduling']:
                        for element in instance['scheduling']['nodeAffinities']:
                            if element['key'] == nodeGroupNameKey:
                                nodeGroupName = element['values'][0]
                            if element['key'] == nodeNameKey:
                                nodeName = element['values'][0]

                    #print(counter, instanceName, instanceId, creationTime, diskCount,
                    #      guestOS, natIP, nodeGroupName, nodeName)
                    data_dict = {'instanceName' : instanceName, 'instanceId' : instanceId, 'creation_time' : creation_time, 
                                'diskCount' : diskCount, 'guestOS':guestOS, 'natIP' : natIP, 
                                'nodeGroupName' : nodeGroupName, 'nodeName':nodeName}
                    temp_df = pd.DataFrame(data_dict, index=[0])
                    instance_df = pd.concat([instance_df,temp_df])
                    counter = counter + 1
                    

        request = service.instances().aggregatedList_next(
            previous_request=request, previous_response=response)
    return instance_df
