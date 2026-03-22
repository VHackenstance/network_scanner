#!usr/bin/env python

from helpers.utils import scan

# Network Scanner Algorithm: Goal -> Discover clients on a Network:
#(1) Create ARP request directed to broadcast MAC asking for IP
scan("192.168.63.2/24") # /24, show clients 192.168.63.(1 - 255)


# 2. Send packet and receive result
# 3. Parse the response
# 4. Print Result


# PROBLEM: ARP requests are logged.
# import logging
# logging.getLogger("scapy").setLevel(logging.CRITICAL)
# This ensures Scapy does not print warnings or informational messages
# Use before running scapy functions like sniff() or sent()