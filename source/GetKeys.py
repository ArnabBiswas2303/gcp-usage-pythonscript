from googleapiclient import discovery
from google.cloud import kms
import pandas as pd


def getKeys(credentials, projectId):
    service = discovery.build('cloudkms', 'v1', credentials=credentials)
    client = kms.KeyManagementServiceClient(credentials=credentials)

    instance_df = pd.DataFrame(columns=['key_name', 'key_version_count'])

    return instance_df
    name = f'projects/{projectId}'
    request = service.projects().locations().list(name=name)
    while True:
        response = request.execute()

        for location in response.get('locations', []):
            locationName = f'projects/{projectId}/locations/{location["locationId"]}'
            keyRings = client.list_key_rings(request={'parent': locationName})

            for keyRing in keyRings:
                cryptoKeys = client.list_crypto_keys(
                    request={'parent': keyRing.name})

                for cryptoKey in cryptoKeys:
                    if str(cryptoKey.primary.state) != 'CryptoKeyVersionState.ENABLED':
                        continue
                    # print(cryptoKey.name)
                    crytoKeyVersion = client.list_crypto_key_versions(
                        request={'parent': cryptoKey.name})
                    count = 0
                    for version in crytoKeyVersion:
                        if str(version.state) == 'CryptoKeyVersionState.ENABLED':
                            count = count + 1
                    if count > 0:
                        data_dict = {'key_name': cryptoKey.name.split(
                            '/')[-1], 'key_version_count': count}
                        temp_df = pd.DataFrame(data_dict, index=[0])
                        instance_df = pd.concat([instance_df, temp_df])

        request = service.projects().locations().list_next(
            previous_request=request, previous_response=response)
        if request is None:
            break

    return instance_df
