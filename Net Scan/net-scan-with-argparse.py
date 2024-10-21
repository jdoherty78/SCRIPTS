#!/usr/bin/env python

import argparse
import scapy.all as scapy



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target ip or network range to scan.")
    options = parser.parse_args()

    if not options.target: 
        parser.error("[x] Please specify an ip address, or network range, use --help for more info.")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []

    for answer in answered_list:
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("-" * 42 + "\nIP\t\t\tMAC Address\n" + "-" * 42)
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_args()

scan_result = scan(options.target)
print_result(scan_result)