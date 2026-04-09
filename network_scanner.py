#!usr/bin/env python

# from utils.nw_scanner_single_function import nw_scanner
# from network_scanner_uncommented import nw_scanner
# nw_scanner()

from helpers.utils import (
    check_for_root, scan, send_receive_response, parse_answered_list,
    print_result, is_valid_iprange, get_arguments )

# Pre step: Accept arguments from user and check format is valid
iprange = get_arguments(is_valid_iprange)

# Make sure sudo is being used
check_for_root()
#(1) Create ARP request to broadcast IP for MAC
broadcast_arp_response_packet = scan(iprange)
#(2) send and receive response
answered_list = send_receive_response(broadcast_arp_response_packet,2, False)
#(3) Parse the results.
results_list = parse_answered_list(answered_list)
#(4) Print result
print_result(results_list)


