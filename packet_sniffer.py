from scapy.all import *

# Function to output packet
def output_packet(packet):
    if Ether in packet:
        ethernet_layer = packet[Ether]
        print(f"Ether Source: {ethernet_layer.src}")
        print(f"Ether Destination: {ethernet_layer.dst}")

    if IP in packet:
        ip = packet[IP]
        print(f"IP Source {ip.src}")
        print(f"IP Destination {ip.dst}")

    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

# Sniff packets on the 'en0' interface
sniff(iface='en0', prn=output_packet)