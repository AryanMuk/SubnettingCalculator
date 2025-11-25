# ip_to_cidr.py

import ipaddress

def ip_to_cidr(ip: str) -> ipaddress.IPv4Network:
    """
    Convert a standard IPv4 address to a network object with default CIDR
    based on class:
        - Class A: /8
        - Class B: /16
        - Class C: /24

    Args:
        ip (str): IPv4 address as string (e.g., "192.168.1.1")

    Returns:
        ipaddress.IPv4Network: network object with CIDR
    """
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
        raise ValueError("IP address is not within Class A/B/C range")
    
    # Convert to IPv4Network object (strict=False allows host IPs)
    network = ipaddress.ip_network(cidr, strict=False)
    return network


# Example usage
if __name__ == "__main__":
    ip_input = input("Enter an IP address: ")
    try:
        network = ip_to_cidr(ip_input)
        print(f"Network with CIDR: {network}")
    except ValueError as ve:
        print(f"Error: {ve}")
