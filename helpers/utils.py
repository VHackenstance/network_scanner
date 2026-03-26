#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import optparse
import os
import re

def check_for_root():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)

#(pre step) get the IP Range as an argument from the User
# Check to see if the IP Range has a valid slash format.
def is_valid_iprange(iprange):
    pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$'
    return bool(re.search(pattern, iprange))

# Get a value from the user for IP Range.
def get_arguments(is_valid_range):
    parser = optparse.OptionParser()
    parser.add_option("-i", "--iprange", dest="iprange", help="IP Range to search for clients / notation.")
    (opt, args) = parser.parse_args()
    if not opt.iprange:
        parser.error("[-] Please specify an IP Range, use --help for more info")
    # Check if the IP Range is valid.
    is_valid = is_valid_range(opt.iprange)
    if not is_valid:
        parser.error("[-] Please use correct format IP Address / slash notation")
    else:
        print("[+] IP Range, " + opt.iprange + ", is valid.")
    return opt.iprange


#(1) Create ARP request directed to broadcast MAC asking for IP
def scan(ip):
    #(a) Create ARP request packet, get MAC from IP
    arp_request = ARP(pdst=ip)
    print(os.linesep + "ARP Request Summary: " + arp_request.summary() + os.linesep)
    #(b) Create ethernet frame (packet) with broadcast MAC
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    print("Broadcast packet summary: " + broadcast.summary() + os.linesep)
    #(c) Combine the broadcast and arp_request packets
    broadcast_arp_request = broadcast / arp_request
    return broadcast_arp_request

#(2) send and receive response
def send_receive_response(packet, timeout, verbose):
    # Option: remove unanswered_list, add [0] end srp call. Keep unanswered contents interesting.
    answered_list, unanswered_list = srp(packet, timeout=timeout, verbose=verbose)
    # print(answered_list.summary())
    # print(unanswered_list.summary())
    return answered_list

#(3) Parse the response - answered - and extract the information we want from it.
def parse_answered_list(answered_list):
    clients_list = []
    for sent, received in answered_list:
        # Capture the results in a list of dictionaries.
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        clients_list.append(client_dict)
    return clients_list

#(4) Print the result
def print_result(results_list):
    print(" IP Address\t\tMAC Address\n ---------------------------------------- ")
    for client in results_list:
        print("", client["ip"] + "\t\t" + client["mac"])
























