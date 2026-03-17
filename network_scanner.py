#!usr/bin/env python

from scapy.layers.l2 import getmacbyip, arping
# import scapy.all as scapy

def scan(ip):
    # mac = getmacbyip(ip)
    # print(mac)
    arping(ip)

scan("192.168.63.2")