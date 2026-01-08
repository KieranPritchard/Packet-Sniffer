from scapy.all import Ether, IP, TCP, sniff

# Function to output packet
def output_packet(packet):
    # Checks if the packet has an ethernet layer
    if Ether in packet:
        # Extracts the ethernet layer
        ethernet_layer = packet[Ether]
        # Outputs the ethernet source and destination address
        print(f"Ether Source: {ethernet_layer.src}")
        print(f"Ether Destination: {ethernet_layer.dst}")

    # Checsk if the packet has an ip layer
    if IP in packet:
        # Extracts the ip layer
        ip = packet[IP]
        # Outputs the ip source and destination address
        print(f"IP Source {ip.src}")
        print(f"IP Destination {ip.dst}")

    # Checks for the tcp layer i the packet
    if TCP in packet:
        # Extracts the ip layer
        tcp_layer = packet[TCP]
        # Outputs the ip source and destination address
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

# Sniff packets on the 'en0' interface
sniff(iface='en0', prn=output_packet)