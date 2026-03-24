#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os

def nw_scanner(ip):
    # Make sure we are using root
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)
    # create ARP request packet, with MAC from IP
    arp_request = ARP(pdst=ip)
    # Create ethernet frame (packet) with broadcast MAC
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the broadcast and arp_request packets
    broadcast_arp_request = broadcast / arp_request
    #(2) send and receive response
    answered_list, unanswered_list = srp(broadcast_arp_request, timeout=2, verbose=False)
    #(3) Parse the response
    for sent, received in answered_list:
        # Get the IP Address
        print(received.psrc)
        # Get the MAC Address
        print(received.hwsrc)
        print("********" + os.linesep)
