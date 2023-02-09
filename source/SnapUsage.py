from googleapiclient import discovery
from datetime import datetime

def getSnaps(credential_object, project_id):
    service = discovery.build('compute', 'v1', credentials=credential_object)
    request = service.snapshots().list(project=project_id)

    while request is not None:
        response = request.execute()

        for snapshot in response['items']:
            is_multi_regional, is_auto_created = False, False
            schedule_policy = '-'

            snap_id = snapshot['id']

            creation_time = snapshot['creationTimestamp'].split('T')[0]
            utc_time = datetime.strptime(creation_time, "%Y-%m-%d")
            epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
            time_obj = datetime.fromtimestamp(epoch_time)
            creation_time = time_obj.strftime("%d %b, %Y")

            snap_name = snapshot['name']
            status = snapshot['status']

            source_disk = snapshot['sourceDisk'].split('/')[-1]
            source_disk_size = snapshot['diskSizeGb']
            storage_byte = snapshot['storageBytes']
            
            snap_loc = snapshot['storageLocations'][0]
            if(len(snap_loc[0].split('-')) == 1):
                is_multi_regional = True
            
            if 'autocreated' in snapshot:
                is_auto_created = True
                schedule_policy = snapshot['sourceSnapshotSchedulePolicy'].split('/')[-1]
            
            print(snap_id, snap_name, creation_time, status, source_disk, source_disk_size, storage_byte, 
                is_multi_regional, snap_loc, is_auto_created, schedule_policy)
            print()

        request = service.snapshots().list_next(previous_request=request, previous_response=response)


