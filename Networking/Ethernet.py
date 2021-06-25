import struct
import socket



class Ethernet:
    def __init__(self, raw_data):
        dest_mac, src_mac, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = self.get_mac_addr(dest_mac)
        self.src_mac = self.get_mac_addr(src_mac)
        self.proto = socket.htons(prototype) 
        self.data = raw_data[14:]
    
    def get_mac_addr(self, bytes_addr):
        bytes_str  = map('{:02x}'.format, bytes_addr)
        return ":".join(bytes_str).upper()
    
    def __str__(self) -> str:
        return f"\t -Destination :{self.dest_mac}\n\t -Source :{self.src_mac}\n\t -Prototype : {self.proto} \n"