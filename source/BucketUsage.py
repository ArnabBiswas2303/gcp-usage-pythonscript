from googleapiclient import discovery
from datetime import datetime
import pandas as pd

def getBuckets(credential_object, project_id):
    service = discovery.build('storage', 'v1', credentials=credential_object)
    request = service.buckets().list(project=project_id)
    count = 0
    col = ['id', 'name', 'projectNumber', 'location', 'location_type', 'storageClass', 'creation_time', 'isDefaultEventBasedHoldEnabled', 
            'rpo', 'isBucketPolicyEnabled', 'isUniformBucketLevelAccessEnabled', 'publicAccessPrevention']
    bucket_df = pd.DataFrame(columns=col)
    bucket_df = bucket_df.astype({'isDefaultEventBasedHoldEnabled':bool,'isBucketPolicyEnabled':bool,
                    'isUniformBucketLevelAccessEnabled':bool})
    while request is not None:
        response = request.execute()
        buckets = response['items']
        isDefaultEventBasedHoldEnabled = False
        rpo = '-'
        
        for bucket in buckets:
            ownerLabel = ''

            # Find owner label
            if 'labels' in bucket:
                if 'owner' in bucket['labels']:
                    ownerLabel = f"owner:{bucket['labels']['owner']}"

            count+=1
            id = bucket['id']
            name = bucket['name']
            projectNumber = bucket['projectNumber']
            location = bucket['location']
            location_type = bucket['locationType']
            storageClass = bucket['storageClass']

            creation_time = bucket['timeCreated'].split('T')[0]
            utc_time = datetime.strptime(creation_time, "%Y-%m-%d")
            epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
            time_obj = datetime.fromtimestamp(epoch_time)
            creation_time = time_obj.strftime("%Y-%m-%d")


            if 'defaultEventBasedHold' in bucket:
                isDefaultEventBasedHoldEnabled = bucket['defaultEventBasedHold']
            if 'rpo' in bucket:
                rpo = bucket['rpo']
            
            iamConfigurations = bucket['iamConfiguration']
            isBucketPolicyEnabled = iamConfigurations['bucketPolicyOnly']['enabled']
            isUniformBucketLevelAccessEnabled = iamConfigurations['uniformBucketLevelAccess']['enabled']
            publicAccessPrevention = iamConfigurations['publicAccessPrevention']

            #print(count, id, name, projectNumber, location, location_type, storageClass, creation_time, isDefaultEventBasedHoldEnabled, 
            #        rpo, isBucketPolicyEnabled, isUniformBucketLevelAccessEnabled, publicAccessPrevention)
            data_dict = {'id':id, 'name':name, 'projectNumber':projectNumber, 'location':location, 
                'location_type':location_type, 'storageClass':storageClass, 'creation_time':creation_time, 
                'isDefaultEventBasedHoldEnabled':isDefaultEventBasedHoldEnabled, 'rpo':rpo, 
                'isBucketPolicyEnabled':isBucketPolicyEnabled, 
                'isUniformBucketLevelAccessEnabled':isUniformBucketLevelAccessEnabled, 
                'publicAccessPrevention':publicAccessPrevention,
                'ownerLabel': ownerLabel}
            temp_df = pd.DataFrame(data_dict, index=[0])
            bucket_df = pd.concat([bucket_df,temp_df])

        request = service.buckets().list_next(previous_request=request, previous_response=response)
    return bucket_df
    


