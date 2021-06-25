from Networking.Ethernet import Ethernet
import socket 
import struct
import textwrap
from Networking.Ethernet import Ethernet
from Networking.Ipv4 import Ipv4
from Networking.Icmp import Icmp
from Networking.Tcp import Tcp
from Networking.Udp import Udp

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('', 9999))
    
    while True:
        raw_data , addr = conn.recvfrom(65565)

        ethernet_head = Ethernet(raw_data)

        print("Ethernet Frame :")
        print(ethernet_head)

        if ethernet_head.proto == 8:
            ipv4_head     = Ipv4(raw_data)
            print("IP Header :")
            print(ipv4_head)

            if ipv4_head.proto == 1:
                icmp_head     = Icmp(raw_data)
                print("ICMP Header :")
                print(icmp_head)
            
            elif ipv4_head.proto == 6:
                tcp_head      = Tcp(raw_data)
                print("TCP Header :")
                print(tcp_head)
                print(tcp_head.show_flags())
            
            elif ipv4_head.proto == 17:
                udp_head     = Udp(raw_data)
                print("UDP Header :")
                print(udp_head)
        


# Need to create for each packet sniffer a class and also create folder to upload schemas of packets.

if __name__ == '__main__':
    main()