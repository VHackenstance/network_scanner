#!usr/bin/env python
from scapy.layers.l2 import ARP

# Network Scanner Algorithm: Goal -> Discover clients on a Network: Setups:

# 1. Create ARP request directed to broadcast MAC asking for IP
    # a. Use ARP to ask who has target IP, test changes for github
def scan(ip):
    # create an ARP packet object
    arp_request = ARP(pdst=ip)
    print(arp_request.summary())


# slash notation /24, show all clients range 192.168.63.1 to 192.168.63.255
scan("192.168.63.2/24")

# b. Set destination MAC to broadcast MAC

# 2. Send packet and receive result
# 3. Parse the response
# 4. Print Result


# PROBLEM: ARP requests are logged.
# import logging
# logging.getLogger("scapy").setLevel(logging.CRITICAL)
# This ensures Scapy does not print warnings or informational messages
# Use before running scapy functions like sniff() or sent()