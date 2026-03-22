#!usr/bin/env python
import scapy.layers.l2 as scapyll2
# import scapy.all as scapy

#(1) Create ARP request directed to broadcast MAC asking for IP
def scan(ip):
    # Use ARP to ask who has target IP, to do so create an ARP packet object.
    arp_request = scapyll2.ARP(pdst=ip)
    # print("Here is our ARP Request Summary: " + arp_request.summary())
    # arp_request.show()

    # Set destination MAC to broadcast MAC, to do so create an Ethernet object.
    broadcast = scapyll2.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print("Here is our Broadcast Summary: " + broadcast.summary())
    # broadcast.show()

    # New packet, combine packets created, using slash "/" notation Scapy feature.
    arp_request_broadcast = broadcast/arp_request
    print("Here is our Broadcast ARP Request Summary: " + arp_request_broadcast.summary())
    arp_request_broadcast.show()