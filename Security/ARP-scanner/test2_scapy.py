from scapy.all import *
conf.use_pcap = True  # Принудительно использовать PCAP
print(conf.use_pcap)  # Должно вывести True