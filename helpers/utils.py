#!usr/bin/env python
from scapy.layers.l2 import Ether, ARP, srp
import os

def check_for_root():
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run again with sudo.")
        exit(1)

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
    print(" IP Address\t\tMAC Address\n ---------------------------------------- ")
    clients_list = []
    for sent, received in answered_list:
        # (4) Print the IP and MAC Address
        print(" " + received.psrc + "\t\t" + received.hwsrc)
        # Capture the results in a list of dictionaries.
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        clients_list.append(client_dict)
    print("\n List of Dictionaries, MAC & IP each host\n ---------------------------------------- ")
    print(clients_list)


