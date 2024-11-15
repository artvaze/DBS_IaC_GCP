from google.cloud import compute_v1
from google.oauth2 import service_account

project = "your-project-id"
zone = "us-central1-a"
network_name = "global/networks/default"
credentials = service_account.Credentials.from_service_account_file("path/to/credentials.json")
instances_client = compute_v1.InstancesClient(credentials=credentials)

# Define the VM instance configuration
def create_instance(instance_name):
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.zone = zone
    instance.machine_type = f"zones/{zone}/machineTypes/e2-micro"
    instance.network_interfaces = [
        compute_v1.NetworkInterface(network=network_name)
    ]
    disk = compute_v1.AttachedDisk()
    disk.auto_delete = True
    disk.boot = True
    disk.initialize_params = compute_v1.AttachedDiskInitializeParams(
        source_image="projects/debian-cloud/global/images/family/debian-10"
    )
    instance.disks = [disk]

    instances_client.insert(
        project=project,
        zone=zone,
        instance_resource=instance
    )
    print(f"Instance {instance_name} created.")

# Create three instances
for i in range(3):
    create_instance(f"my-instance-{i}")
