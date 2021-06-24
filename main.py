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


def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind(('', 9999))
    
    while True:
        raw_data , addr = conn.recvfrom(65565)
        dest_mac, src_mac, proto, data = ethernet_head(raw_data)

        print("Ethernet Frame :")
        print(f"\t Destination :{dest_mac}\n\t Source :{src_mac}\n\t Prototype : {proto}\n\t Data :{data}")


if __name__ == '__main__':
    main()