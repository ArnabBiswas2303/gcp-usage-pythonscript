from googleapiclient import discovery
from datetime import datetime
import pandas as pd

def getStaticIP(credential_object, project_id):
    count=0
    service = discovery.build('compute', 'v1', credentials=credential_object)
    request = service.addresses().aggregatedList(project=project_id)
    col = ['address_id', 'name', 'ip', 'status', 'creation_time', 'region', 'instance']
    ips_df = pd.DataFrame(columns=col)
    while request is not None:
        response = request.execute()
        for name, addresses_scoped_list in response['items'].items():
            #skip if global
            if name == 'global':
                continue
            #skip if no IP exists in region
            if 'warning' in addresses_scoped_list:
                continue
            address_list = addresses_scoped_list['addresses']
            instance = '-'
            for address in address_list:

                # global variables
                address_id = address['id']
                creation_time = address['creationTimestamp'].split('T')[0]
                utc_time = datetime.strptime(creation_time, "%Y-%m-%d")
                epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
                time_obj = datetime.fromtimestamp(epoch_time)
                creation_time = time_obj.strftime("%Y-%m-%d")
                instance = '-'

                #skip if address type is INTERNAL
                if address['addressType'] == "INTERNAL":
                    continue
                count+=1
                if 'users' in address:
                    #skip if forwarding rule
                    if address['users'][0].split('/')[-2] != 'instances':
                        continue
                    instance = address['users'][0].split('/')[-1]

                name = address['name']
                ip = address['address']
                region = address['region'].split('/')[-1]
                status = address['status']

                #print(count, address_id, name, ip, status, creation_time, region, instance)
                data_dict = {'address_id':address_id, 'name':name, 'ip':ip, 
                            'status':status, 'creation_time':creation_time, 'region':region, 'instance':instance}
                temp_df = pd.DataFrame(data_dict, index=[0])
                ips_df = pd.concat([ips_df,temp_df])

        request = service.addresses().aggregatedList_next(previous_request=request, previous_response=response)
    return ips_df


