import socket 
import struct
import textwrap

def ethernet_head(raw_data):
    #  the first 14 bytes (6 bytes 6 bytes H:2 small unsigned int)
    dest_mac, src_mac, prototype = struct.unpack('! 6s 6s H', raw_data[:14])
    dest_mac = get_mac_addr(dest_mac)
    src_mac = get_mac_addr(src_mac)
    proto = socket.htons(prototype) 
    data = raw_data[14:]

    return dest_mac, src_mac, proto, data


def get_mac_addr(bytes_addr):
    bytes_str  = map('{:02x}'.format, bytes_addr)
    return ":".join(bytes_str).upper()

def ipv4_head(raw_data):
    version_header_lenght = raw_data[0]
    version = version_header_lenght >> 4
    header_lenght = (version_header_lenght & 15) * 4

    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])

    return version, header_lenght, ttl, proto, ipv4(src), ipv4(target), raw_data[20:]

def ipv4(addr):
    return ".".join(map(str, addr))


def icmp_packet(raw_data):
    icmp_type, code, checksum = struct.unpack('! B B H',raw_data[:4])
    return icmp_type, code, checksum, raw_data[4:]

def tcp_packet(raw_data):
    src_port, dest_port, sequence, acknowledgment, offset_reserved_flags = struct.unpack('! H H L L H',raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 5
    flag_psh = (offset_reserved_flags & 8) >> 5
    flag_rst = (offset_reserved_flags & 4) >> 5
    flag_syn = (offset_reserved_flags & 2) >> 5
    flag_fin = offset_reserved_flags & 1

    return src_port, dest_port, sequence, acknowledgment, offset, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('', 9999))
    
    while True:
        raw_data , addr = conn.recvfrom(65565)
        dest_mac, src_mac, proto, data = ethernet_head(raw_data)

        version, header_lenght, ttl, prototype, src, target, dataI = ipv4_head(raw_data)

        print("Ethernet Frame :")
        print(f"\t Destination :{dest_mac}\n\t Source :{src_mac}\n\t Prototype : {proto} \n")

        print("IP Header :")
        print(f"\t Version: {version}\n\t Header_lenght :{header_lenght}\n\t TTL : {ttl}\n\t"
         f" Prototype : {prototype}\n\t Source : {src}\n\t Target : {target}\n")


# Need to create for each packet sniffer a class and also create folder to upload schemas of packets.
# Ideas : https://github.com/molansec/PassiveScanner/tree/fe8fc3a9465367d5440c1c1927a62386756cb371
# https://www.youtube.com/watch?v=3zwuOo7U1YQ&ab_channel=thenewboston
# https://www.uv.mx/personal/angelperez/files/2018/10/sniffers_texto.pdf

if __name__ == '__main__':
    main()