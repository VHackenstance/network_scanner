#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os

def nw_scanner(ip):
    if os.geteuid() != 0:                           # Make sure we use root
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)
    #(1) Create ARP request to broadcast IP for MAC
    arp_request = ARP(pdst=ip)                      # create ARP request packet
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")      # Create ethernet frame with broadcast MAC
    broadcast_arp_request = broadcast / arp_request # Combine the broadcast and arp_request packets
    #(2) Send and receive response
    answered_list, unanswered_list = srp(broadcast_arp_request, timeout=2, verbose=False)
    #(3) Parse response
    clients_list = []
    for sent, received in answered_list:
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        clients_list.append(client_dict)
    #(4) Print response
    print(" IP Address\t\tMAC Address\n ---------------------------------------- ")
    for client in clients_list:
        print("", client["ip"] + "\t\t" + client["mac"])
