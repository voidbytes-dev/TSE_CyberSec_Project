import os
import logging
import time
import socket
import scapy.all as scapy # importing necessary modules

bool isUnderAttack = false      #   Bool that will switch based on monitoring
ipCounts = {}           # ip counter against threshold
threshold = 0           # Threshold to be decided with team
suspicious = []         # List of suspicious IPs

# Setting up logger, handler and formatting for the log
def attackLogger():
    logger = logging.GetLogger("detector")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatting = logging.Formatter('%(levelname)s: %(message)s [%(asctime)s]')
    handler.setFormatter(formatting)
    logger.addHandler(handler)
    return

def trafficMonitor(isUnderAttack, ipCounts, suspicious, threshold):
    while isUnderAttack == false:
        packets = PcapReader("capture.pcap")       # Captures and reads packets
        for packet in packets:
            if packet.hasLayer(DNS) and packet[DNS].qr == 1 and packet[DNS].ancount == 0:   # Checks if the DNS responds using a query (qr)
                ip = packet[IP].dst
                ipCounts[ip] = ipCounts.get(ip, 0) + 1
        for ip, instances in ipCounts.items():              # checks count against threshold and decides whether to add it to the list or pass
            if instances < threshold:
                continue
            else:
                suspicious.append(ip)
               