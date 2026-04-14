#!usr/bin/env python

from helpers.utils import (
    check_for_root, scan, send_receive_response, parse_answered_list,
    print_result, is_valid_iprange, get_arguments )

iprange = get_arguments(is_valid_iprange) # Pre step: Accept arguments from user,check valid format
check_for_root() # Make sure sudo is being used
broadcast_arp_response_packet = scan(iprange) #(1) Create ARP request to broadcast IP for MAC
answered_list = send_receive_response(broadcast_arp_response_packet,2, False) #(2) send and receive response
results_list = parse_answered_list(answered_list) #(3) Parse the results.
print_result(results_list) #(4) Print result


