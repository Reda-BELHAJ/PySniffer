from Networking.Ethernet import Ethernet
import socket 
import struct
import textwrap
from Networking.Ethernet import Ethernet
from Networking.Ipv4 import Ipv4
from Networking.Icmp import Icmp
from Networking.Tcp import Tcp


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('', 9999))
    
    while True:
        raw_data , addr = conn.recvfrom(65565)

        ethernet_head = Ethernet(raw_data)
        ipv4_head     = Ipv4(raw_data)
        icmp_head     = Icmp(raw_data)
        tcp_head      = Tcp(raw_data)

        print("Ethernet Frame :")
        print(ethernet_head)

        print("IP Header :")
        print(ipv4_head)

        print("ICMP Header :")
        print(icmp_head)

        print("TCP Header :")
        print(tcp_head)
        print(tcp_head.show_flags())
        


# Need to create for each packet sniffer a class and also create folder to upload schemas of packets.

if __name__ == '__main__':
    main()