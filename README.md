# GCP USAGE SCRIPT

## Environment Setup

Add the following environment variables

> GCP_SCRIPT_JSON_KEY_PATH => Path to JSON Key
> GCP_SCRIPT_EMAIL_TO => Senders email
> GCP_SCRIPT_EMAIL_FROM => Receivers email

## Required Library Installation

- pip install google-api-python-client
- pip install google-cloud-storage
- pip install pywin32
- pip install google-cloud-kms
- pip install pandas
- pip install Jinja2
- pip install openpyxl

## Required Permission For Service Account

- cloudkms.cryptoKeyVersions.list
- cloudkms.cryptoKeys.list
- cloudkms.keyRings.list
- cloudkms.locations.list
- compute.addresses.list
- compute.diskTypes.get
- compute.diskTypes.list
- compute.disks.get
- compute.disks.list
- compute.instances.get
- compute.instances.list
- compute.snapshots.list
- compute.nodeGroups.list
- storage.buckets.get
- storage.buckets.getIamPolicy
- storage.buckets.list
- resourcemanager.projects.get
- iam.serviceAccounts.get

  ### To Run: `python .\source\init.py`
