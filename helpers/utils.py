#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
# import scapy.all as scapy

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
    answered, unanswered = srp(packet, iface="eth0", timeout=2, verbose=False)
    print(answered.summary())

