import os
import logging
import time
import socket
import scapy # importing necessary modules

isUnderAttack = False      #   Bool that will switch based on monitoring
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

def trafficMonitor(isUnderAttack, ipCounts, suspicious, threshold):
        packets = scapy.PcapReader("capture.pcap")       # Captures and reads packets
        for packet in packets:
            if packet.hasLayer(scapy.DNS) and packet[scapy.DNS].qr == 1 and packet[scapy.DNS].ancount == 0:   # Checks if the DNS responds using a query (qr)
                ip = packet[scapy.IP].dst
                ipCounts[ip] = ipCounts.get(ip, 0) + 1
        for ip, instances in ipCounts.items():              # checks count against threshold and decides whether to add it to the list or pass
            if instances < threshold:
                continue
            else:
                suspicious.append(ip)
                for i in suspicious:
                    if i >= threshold:
                        isUnderAttack = True           # Sets isUnderAttack to True is number of suspicious IPs reaches or exceeds the threshold

def attackBlocker(isUnderAttack, ipCounts, threshold, suspicious):
    while isUnderAttack == False:
        pass
    while isUnderAttack == True:
        pass # gonna write this out later