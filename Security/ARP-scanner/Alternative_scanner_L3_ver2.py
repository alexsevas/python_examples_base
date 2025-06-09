from scapy.all import srp, Ether, ARP, conf

conf.L3socket  # должен быть задан автоматически
conf.L3socket6

# Пример ARP-скана с использованием L3
def scan():
    ip_range = "192.168.1.0/24"
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

print(scan())