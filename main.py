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
    bytes_addr = map()