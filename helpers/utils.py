#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os
# import scapy.all as scapy

def check_for_root():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)

#(1) Create ARP request directed to broadcast MAC asking for IP
def scan(ip):
    # create ARP request packet
    arp_request = ARP(pdst=ip)
    # print(arp_request.summary())

    # Create ethernet frame with broadcast MAC
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())

    # Combine packets
    packet = broadcast / arp_request
    # packet.show()

    # send and receive response
    ##### IMPORTANT!!!! #####
    ##### This step requires we run the script with SUDO #####
    # Updated: have introduced a code snippet to protect for this.
    answered, unanswered = srp(packet, iface="eth0", timeout=2, verbose=False)
    print(answered.summary())

