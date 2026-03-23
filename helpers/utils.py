#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os
# import scapy.all as scapy

def check_for_root():
    # Require root use as scapy srp needs sudo for step 2: Send and receive a response.
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

    # Combine the broadcast and arp_request packets
    broadcast_arp_request = broadcast / arp_request
    # packet.show()
    return broadcast_arp_request

#(2) send and receive response
def send_receive_response(packet, iface, timeout, verbose):
    # iface argument may not be needed.
    answered, unanswered = srp(packet, iface=iface, timeout=timeout, verbose=verbose)
    print(answered.summary())
    return answered

#(3) Parse the response - answered - and extract the information we want from it.

