#!usr/bin/env python
import scapy.layers.l2 as scapyll2
# import scapy.all as scapy

# Network Scanner Algorithm: Goal -> Discover clients on a Network: Setups:
#(1) Create ARP request directed to broadcast MAC asking for IP
def scan(ip):
    #(a) Use ARP to ask who has target IP, to do so create an ARP packet object.
    arp_request = scapyll2.ARP(pdst=ip)
    print("Here is our ARP Request Summary: " + arp_request.summary())
    arp_request.show()

    #(b) Set destination MAC to broadcast MAC, to do so create an Ethernet object.
    broadcast = scapyll2.Ether(dst="ff:ff:ff:ff:ff:ff")
    print("Here is our Broadcast Summary: " + broadcast.summary())
    broadcast.show()

    # Create new packet, combine packets created, using slash "/" notation Scapy feature.
    arp_request_broadcast = broadcast/arp_request
    print("Here is our Broadcast ARP Request Summary: " + arp_request_broadcast.summary())
    arp_request_broadcast.show()
    
    # Create ethernet frame to be sent to the broadcast MAC address


# slash notation /24, show all clients range 192.168.63.1 to 192.168.63.255
scan("192.168.63.2/24")

# 2. Send packet and receive result
# 3. Parse the response
# 4. Print Result


# PROBLEM: ARP requests are logged.
# import logging
# logging.getLogger("scapy").setLevel(logging.CRITICAL)
# This ensures Scapy does not print warnings or informational messages
# Use before running scapy functions like sniff() or sent()