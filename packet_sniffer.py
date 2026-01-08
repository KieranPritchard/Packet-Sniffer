from scapy.all import *

# Function to output packet
def output_packet(packet):
    if Ether in packet:
        ethernet_layer = packet[Ether]
        print(f"Source destination: {ethernet_layer.src}")
        print(f"Destination Port: {ethernet_layer.dst}")

    if IP in packet:
        ip = packet[IP]
        print(f"IP  {ip.src} → {ip.dst}")

    if TCP in packet:
        tcp_layer = packet[TCP]
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

# Sniff packets on the 'eth0' interface
sniff(iface='en0', prn=output_packet)