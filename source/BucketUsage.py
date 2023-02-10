from googleapiclient import discovery
from datetime import datetime

def getBuckets(credential_object, project_id):
    service = discovery.build('storage', 'v1', credentials=credential_object)
    request = service.buckets().list(project=project_id)
    count = 0

    while request is not None:
        response = request.execute()
        buckets = response['items']
        isDefaultEventBasedHoldEnabled = False
        rpo = '-'
        for bucket in buckets:
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
            creation_time = time_obj.strftime("%d %b, %Y")


            if 'defaultEventBasedHold' in bucket:
                isDefaultEventBasedHoldEnabled = bucket['defaultEventBasedHold']
            if 'rpo' in bucket:
                rpo = bucket['rpo']
            
            iamConfigurations = bucket['iamConfiguration']
            isBucketPolicyEnabled = iamConfigurations['bucketPolicyOnly']['enabled']
            isUniformBucketLevelAccessEnabled = iamConfigurations['uniformBucketLevelAccess']['enabled']
            publicAccessPrevention = iamConfigurations['publicAccessPrevention']

            print(count, id, name, projectNumber, location, location_type, storageClass, creation_time, isDefaultEventBasedHoldEnabled, 
                    rpo, isBucketPolicyEnabled, isUniformBucketLevelAccessEnabled, publicAccessPrevention)
            print()

        request = service.buckets().list_next(previous_request=request, previous_response=response)
    


