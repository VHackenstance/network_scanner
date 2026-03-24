#!usr/bin/env python
from helpers.utils import scan, check_for_root,  send_receive_response, parse_answered_list
# from helpers.nw_scanner_single_function import nw_scanner

check_for_root()
#(1) Create ARP request directed to broadcast MAC asking for IP
broadcast_arp_response_packet = scan("192.168.1.254/24")
#(2) send and receive response
answered_list = send_receive_response(broadcast_arp_response_packet, "", 2, False)
#(3) Parse the results, from two lists, answered and unanswered.
parse_answered_list(answered_list)

# nw_scanner("192.168.1.254/24")
