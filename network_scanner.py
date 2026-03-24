#!usr/bin/env python
from helpers.utils import scan, check_for_root,  send_receive_response

check_for_root()
#(1) Create ARP request directed to broadcast MAC asking for IP
broadcast_arp_response_packet = scan("192.168.1.254/24")
#(2) send and receive response
send_receive_response(broadcast_arp_response_packet, "", 2, False)
#(3) Parse the results, from two lists, answered and unanswered.
