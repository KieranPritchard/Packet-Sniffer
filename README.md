# Packet Sniffer

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Packet-Sniffer">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Packet-Sniffer">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Packet-Sniffer">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Packet-Sniffer">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Packet-Sniffer">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Packet-Sniffer">

</div>

## Project Description

### Objective:

To create a basic packet sniffer to practise using Python’s Scapy library, allowing me to capture live network traffic and then dissect individual packets to extract information such as source and destination IP addresses and port numbers. The goal of this project is to strengthen my understanding of how packet sniffing works, become more comfortable using Scapy’s core features, and build a solid foundation for developing more advanced networking, monitoring, and security-related scripts and projects in the future.

### Technology and Tools Used:

* **Language:** Python
* **Framework/Library:** Scapy
* **Tools:** VS Code, Git

### Challenges Faced:

The only issue I ran into was identifying the correct network interface to sniff packets on. This was resolved by checking my network configuration using ipconfig, which allowed me to find the appropriate interface to use.

### Outcome:

By the end of this project, I successfully created a basic packet sniffer that captures live network traffic and extracts key information such as source and destination IP addresses along with port numbers. This helped me get hands-on experience with Scapy’s packet sniffing and packet dissection features, and better understand how data moves across a network. Overall, this project gave me a solid foundation to build more advanced networking scripts and security-related tools in the future.

## How to Use the Project
1. **Clone the Repository:**
- Download the project to your local machine. This can be done using Git to clone the repository.
2. **Configure the Network Interface:**
- Before running the script, identify the correct network interface to sniff packets on.
- This can be found by checking your network configuration (e.g. using ipconfig or ifconfig).
- Update the iface value in the script (e.g. iface='en0') to match your system.
3. **Understanding the Script:**
- The script uses Scapy to sniff live network traffic.
- It checks each captured packet for Ethernet, IP, and TCP layers.
- When present, it outputs source and destination MAC addresses, IP addresses, and port numbers.
4. **Running the Script:**
- Navigate to the directory containing the script.
- Run the script using: python packet_sniffer.py
- Packet information will be printed to the terminal in real time as traffic is captured.
5. **Stopping the Sniffer:**
- To stop packet capture, interrupt the program using Ctrl + C.

## Licenses
License is located in the root of the repositor