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


if __name__ == '__main__':
    main()