#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import optparse
import os
import re

def nw_scanner():
    if os.geteuid() != 0:                           # Make sure we use root
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)
    # Get a value from the user for IP Range.
    parser = optparse.OptionParser()
    parser.add_option("-i", "--iprange", dest="iprange", help="IP Range to search for clients / notation.")
    (opt, args) = parser.parse_args()
    if not opt.iprange:
        parser.error("[-] Please specify an IP Range, use --help for more info")
    # Check if the IP Range is valid.
    pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$'
    is_valid = bool(re.search(pattern, opt.iprange))
    if not is_valid:
        parser.error("[-] Please use correct format IP Address / slash notation")
    else:
        print("[+] IP Range, " + opt.iprange + ", is valid.")
    ip = opt.iprange
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
