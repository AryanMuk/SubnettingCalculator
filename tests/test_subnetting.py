import ipaddress
import pytest
from subnettingcalculator.subnetting import subnetting_calculator

def test_ip_to_cidr_basic():
    # Test một IP chuẩn
    ip = "192.168.1.0/24"
    net = ipaddress.ip_network(ip)
    assert str(net.network_address) == "192.168.1.0"
    assert net.prefixlen == 24
