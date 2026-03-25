#!usr/bin/env python
# from helpers.nw_scanner_single_function import nw_scanner
# nw_scanner("192.168.1.254/24")
from helpers.utils import check_for_root, scan, send_receive_response, parse_answered_list

check_for_root()
#(1) Create ARP request to broadcast IP for MAC
broadcast_arp_response_packet = scan("192.168.1.254/24")
#(2) send and receive response
answered_list = send_receive_response(broadcast_arp_response_packet,2, False)
#(3) Parse the results.  #(4) Print result
parse_answered_list(answered_list)


