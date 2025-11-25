# ec2_ip_fetcher.py

import boto3

def get_running_ec2_ips():
    """
    Fetch running EC2 instances' IDs, public IPs, and private IPs.
    Returns a list of dictionaries for each instance.
    """
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    except Exception as e:
        print(f"Error fetching EC2 instances: {e}")
        return []

    instances_info = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            public_ip = instance.get('PublicIpAddress', 'N/A')
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            
            instances_info.append({
                'Instance ID': instance_id,
                'State': state,
                'Public IP': public_ip,
                'Private IP': private_ip
            })
    
    return instances_info


def display_ec2_ips(instances_info):
    """
    Nicely display EC2 instances IP information.
    """
    if not instances_info:
        print("No running EC2 instances found.")
        return
    
    print("\nRunning EC2 Instances:")
    for inst in instances_info:
        print(f"Instance ID: {inst['Instance ID']}")
        print(f"  State: {inst['State']}")
        print(f"  Public IPv4: {inst['Public IP']}")
        print(f"  Private IPv4: {inst['Private IP']}")
        print("------")


# Example usage:
if __name__ == "__main__":
    instances = get_running_ec2_ips()
    display_ec2_ips(instances)
