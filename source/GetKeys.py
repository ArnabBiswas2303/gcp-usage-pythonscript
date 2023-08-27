import requests
import pandas as pd


def getKeys(credentials, projectId):

    # make sure kmsInventoryAPI is enabled for the given project.
    kmsInventoryURL = f"https://kmsinventory.googleapis.com/v1/projects/{projectId}/cryptoKeys"
    headers = {
        "Authorization": f"Bearer {credentials.token}"
    }
    response = requests.get(kmsInventoryURL, headers=headers)

    instance_df = pd.DataFrame(columns=['key_name'])
    if response.status_code != 200:
        print(response.json())
        return instance_df

    for key in response.json()['cryptoKeys']:
        keyName = key['name'].split('/')[-1]
        consider_this_key = 0
        if 'primary' in key:
            if key['primary']['state'] == 'ENABLED':
                consider_this_key = 1
        else:
            consider_this_key = 1

        if consider_this_key == 1:
            data_dict = {'key_name': keyName}
            temp_df = pd.DataFrame(data_dict, index=[0])
            instance_df = pd.concat([instance_df, temp_df])

    return instance_df
