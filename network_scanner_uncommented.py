#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import argparse
import os
import re

# My eth0 ip is 192.168.1.234
# So run ifconfig locally and select the ip you want to broadcast range

def nw_scanner():
    if os.geteuid() != 0:
        print("Script requires root. Use sudo.")
        exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iprange", dest="iprange", help="IP Range to search for clients /notation.")
    options = parser.parse_args()
    if not options.iprange:
        parser.error("[-] Please specify an IP Range, use --help for more info")
    pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$'
    is_valid = bool(re.search(pattern, options.iprange))
    if not is_valid:
        parser.error("[-] Please use correct format IP Address / slash notation")
    arp_request = ARP(pdst=options.iprange)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast/arp_request
    answered_list, unanswered_list = srp(broadcast_arp_request, timeout=2, verbose=False)
    clients_list = []
    for sent, received in answered_list:
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        clients_list.append(client_dict)
    for client in clients_list:
        print("", client["ip"] + "\t\t" + client["mac"])