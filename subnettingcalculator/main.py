# main.py
import boto3
from tabulate import tabulate
import ipaddress
import math

from ec2_ip_fetcher import get_ec2_ips
from ip_to_cidr import ip_to_cidr
from subnetting import subnetting_calculator

def main():
    print("===== Advanced IPv4 Subnet Calculator (AWS Cloud9) =====")

    while True:
        try:
            inp1 = int(input('''
Enter [1] to enter an IP address
Enter [2] to use your EC2 server IP address
Enter [0] to exit
Your choice: '''))

            if inp1 == 0:
                print("Exiting...")
                break

            elif inp1 == 1:
                cidr = input("Enter Required IP Address in CIDR format: ")
                subnetting_calculator(cidr)

            elif inp1 == 2:
                ec2_ips = get_ec2_ips()
                if not ec2_ips:
                    print("No running EC2 instances found.")
                    continue

                print("\nDetected EC2 instances:")
                for i, instance in enumerate(ec2_ips, 1):
                    print(f"{i}. Instance ID: {instance['InstanceId']}")
                    print(f"   State: {instance['State']}")
                    print(f"   Public IPv4: {instance['PublicIp']}")
                    print(f"   Private IPv4: {instance['PrivateIp']}\n")

                inp2 = input("Use [private] or [public] IP for subnetting? ").strip().lower()
                if inp2 not in ["private", "public"]:
                    print("Invalid choice. Run again.")
                    continue
                selected_ip = ec2_ips[0]['PrivateIp'] if inp2 == "private" else ec2_ips[0]['PublicIp']
                cidr_network = ip_to_cidr(selected_ip)
                subnetting_calculator(cidr_network)

            else:
                print("Invalid choice. Enter 0, 1, or 2.")

        except ValueError:
            print("Invalid input. Enter a number only.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
