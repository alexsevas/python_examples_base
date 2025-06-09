# conda activate allpy310
# pip install scapy

from scapy.all import ARP, Ether, srp
import time

def scan(ip_range="192.168.1.0/24"):
    print(f"📡 Сканирование сети {ip_range}...")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def print_devices(devices):
    print("💻 Обнаруженные устройства:")
    for d in devices:
        print(f"{d['ip']}  ➜  {d['mac']}")

def detect_spoof(devices):
    macs = {}
    for dev in devices:
        if dev['mac'] in macs:
            print("⚠️ Возможный ARP-спуфинг!")
            print(f"IP-адреса {macs[dev['mac']]} и {dev['ip']} имеют одинаковый MAC: {dev['mac']}")
        else:
            macs[dev['mac']] = dev['ip']

if __name__ == "__main__":
    while True:
        devs = scan()
        print_devices(devs)
        detect_spoof(devs)
        print("⏳ Следующий цикл через 30 секунд...\n")
        time.sleep(30)
