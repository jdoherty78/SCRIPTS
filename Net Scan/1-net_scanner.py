#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

# scan("192.168.80.1")
scan("192.168.80.1/24")