import requests
import pandas as pd


def getNodeGroup(credentials, projectId):
    # required columns
    col = ['node_group', 'creation_time', 'location']

    # make sure node group api is enabled for the given project.
    nodeGroupAggListURL = f"https://compute.googleapis.com/compute/v1/projects/{projectId}/aggregated/nodeGroups"
    headers = {
        "Authorization": f"Bearer {credentials.token}"
    }

    response = requests.get(nodeGroupAggListURL, headers=headers)

    nodegroup_df = pd.DataFrame(columns=col)
    if response.status_code != 200:
        return nodegroup_df

    nodeGroupList = response.json()['items']
    for zone in nodeGroupList:
        if 'warning' in nodeGroupList[zone]:
            continue

        nodeGroupName, creationTime, location = '', '', ''
        zoneOrRegion = zone.split('/')[-1]

        for nodeGroup in nodeGroupList[zone]['nodeGroups']:
            nodeGroupName = nodeGroup['name']
            creationTime = nodeGroup['creationTimestamp']
            location = zoneOrRegion

            data_dict = {
                'node_group': nodeGroupName,
                'creation_time': creationTime,
                'location': location
            }

            temp_df = pd.DataFrame(data_dict, index=[0])
            nodegroup_df = pd.concat([nodegroup_df, temp_df])

    return nodegroup_df
