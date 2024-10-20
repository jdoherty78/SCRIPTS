#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    for answer in answered_list:
        print(answer[1].psrc)
        print(answer[1].hwsrc)
        print("-" * 20)


scan("10.0.0.1/24")