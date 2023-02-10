from googleapiclient import discovery
from google.cloud import kms


def getLocations(credentials, projectId):
    service = discovery.build('cloudkms', 'v1', credentials=credentials)
    client = kms.KeyManagementServiceClient(credentials=credentials)

    allCryptoKeys = []

    name = f'projects/{projectId}'
    request = service.projects().locations().list(name=name)
    while True:
        response = request.execute()

        for location in response.get('locations', []):
            locationName = f'projects/{projectId}/locations/{location["locationId"]}'
            if locationName == 'us-east1':
                print('got the location')

            keyRings = client.list_key_rings(request={'parent': locationName})
            for keyRing in keyRings:

                if keyRing == 'abiswasRegKeyRing':
                    print('got keyring')
                cryptoKeys = client.list_crypto_keys(
                    request={'parent': keyRing.name})
                for cryptoKey in cryptoKeys:

                    print(cryptoKey.name)
                    crytoKeyVersion = client.list_crypto_key_versions(
                        request={'parent': cryptoKey.name})
                    count = 0
                    for version in crytoKeyVersion:
                        count = count + 1
                    allCryptoKeys.append(
                        [cryptoKey.name.split('/')[-1], count])

        request = service.projects().locations().list_next(
            previous_request=request, previous_response=response)
        if request is None:
            break
    print(allCryptoKeys)


def getKeys(credentials, projectId):

    getLocations(credentials, projectId)
