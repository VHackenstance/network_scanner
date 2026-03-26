#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os

def nw_scanner(ip):
    if os.geteuid() != 0:
        print("Script requires root. Use sudo.")
        exit(1)
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast/arp_request
    answered_list, unanswered_list = srp(broadcast_arp_request, timeout=2, verbose=False)
    clients_list = []
    for sent, received in answered_list:
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        clients_list.append(client_dict)
    for client in clients_list:
        print("", client["ip"] + "\t\t" + client["mac"])