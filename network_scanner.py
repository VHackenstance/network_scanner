#!usr/bin/env python

from scapy.layers.l2 import getmacbyip, arping
# import scapy.all as scapy

def scan(ip):
    # mac = getmacbyip(ip)
    # print(mac)
    arping(ip)

# add slash notation /24 to show all clients in range 192.168.63.1 to 192.168.63.255
scan("192.168.63.2/24")

# Network Scanner Algorithm
# Goal -> Discover clients on a Network
# Setups:
# 1. Create ARP request directed to broadcast MAC asking for IP
# 2. Send packet and receive result
# 3. Parse the response
# 4. Print Result


# PROBLEM: ARP requests are logged.
# import logging
# logging.getLogger("scapy").setLevel(logging.CRITICAL)
# This ensures Scapy does not print warnings or informational messages
# Use before running scapy functions like sniff() or sent()