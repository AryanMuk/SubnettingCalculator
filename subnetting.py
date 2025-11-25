import boto3
import ipaddress
from tabulate import tabulate
import math

public_ip = None
private_ip = None
def get_ips():
    global public_ip
    global private_ip
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            publicip = instance.get('PublicIpAddress', 'N/A')
            public_ip = publicip
            privateip = instance.get('PrivateIpAddress', 'N/A')
            private_ip = privateip
            state = instance['State']['Name']

            print(f"Instance ID: {instance_id}")
            print(f"  State: {state}")
            print(f"  Public IPv4: {public_ip}") 
            print(f"  Private IPv4: {private_ip}") 
            print("------")



def subnetting_calculator(cidr):
    print("\n===== Subnetting Calculator =====")
    mode = input("Do you want to enter number of (n) networks or (h) hosts? [n/h]: ").lower()
    
    if mode not in ["n", "h"]:
        print("Invalid choice. Enter 'n' or 'h'.")
        return

    # Convert base network
    try:
        base = ipaddress.ip_network(cidr, strict=False)
    except ValueError:
        print("Invalid CIDR format.")
        return

    original_prefix = base.prefixlen
    max_hosts_original = (2 ** (32 - original_prefix)) - 2

    # Calculate based on mode
    if mode == "n":
        required_subnets = int(input("Enter number of networks needed: "))
        bits_needed = math.ceil(math.log2(required_subnets))
        new_prefix = original_prefix + bits_needed

    else:  # host-based
        required_hosts = int(input("Enter number of hosts needed per subnet: "))
        bits_needed = math.ceil(math.log2(required_hosts + 2))      # +2 for network + broadcast
        new_prefix = 32 - bits_needed

        if new_prefix < original_prefix:
            print("ERROR: Required hosts exceed block capacity.")
            return

    # Create subnets
    subnets = list(base.subnets(new_prefix=new_prefix))

    # Prepare results
    table = []
    for i, sn in enumerate(subnets):
        network = sn.network_address
        broadcast = sn.broadcast_address
        all_hosts = list(sn.hosts())
        
        first_host = all_hosts[0]
        last_host = all_hosts[-1]
        total_hosts = len(all_hosts)

        table.append([
            i + 1,
            str(sn),
            str(network),
            str(broadcast),
            str(first_host),
            str(last_host),
            total_hosts
        ])

    print("\n===== Subnetting Result =====\n")
    print(tabulate(
        table,
        headers=["Subnet #", "CIDR", "Network ID", "Broadcast ID", "First Host", "Last Host", "Total Usable Hosts"],
        tablefmt="grid"
    ))

import ipaddress

def ip_to_cidr(ip): #converts the regular address to CIDR
    # Determine class and set default mask/prefix
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        # Class A
        cidr = f"{ip}/8"
    elif 128 <= first_octet <= 191:
        # Class B
        cidr = f"{ip}/16"
    elif 192 <= first_octet <= 223:
        # Class C
        cidr = f"{ip}/24"
    else:
        raise ValueError("IP address is not within the Class A/B/C range")

    # Validate and return network in CIDR
    network = ipaddress.ip_network(cidr, strict=False)
    return network




while True:
    inp1 = int(input('''
Enter [1] to enter an IP address 
Enter [2] to use your EC2 server IP address
'''))

    if inp1 == 1:
        cidr = input("Enter Required IP Address in CIDR format : ")
        subnetting_calculator(cidr)
    elif inp1 == 2:              
        get_ips()
        inp2 = input("Would you like to use the private address or public address? [private/public] : ")
        if inp2 == "public":
            cidr = public_ip
            subnetting_calculator(ip_to_cidr(cidr))
        elif inp2 == "private":
            cidr = private_ip
            subnetting_calculator(ip_to_cidr(cidr))
        else:
            print("Invalid, run again")
            break
    else:
        print('Invalid, run again')
        break