import Authentication

project_id = 'vsa-dev-298916'
jsonKeyLocation = '/Users/abiswas/Desktop/LOGS/IAM_JSON/vsa-dev-298916-7a558f236b34.json'


credentialObject = Authentication.getAuth(project_id, jsonKeyLocation)
print(credentialObject)
