from scapy.all import *
import ipaddress

def ping_scan(network):
    live_hosts = []
    for ip in ipaddress.IPv4Network(network):
        packet = IP(dst=str(ip))/ICMP()
        response = sr1(packet, timeout=1, verbose=0)
        if response:
            live_hosts.append(str(ip))
    return live_hosts

# Использование
devs = ping_scan("192.168.1.0/24")
print("Active hosts:", devs)