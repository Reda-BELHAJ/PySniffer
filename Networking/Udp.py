import struct


class Udp:
    def __init__(self, raw_data):
        self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', raw_data[:8])
        self.data = raw_data[8:]
    
    def __str__(self) -> str:
        return f"\t -Destination :{self.dest_mac}\n\t -Source :{self.src_mac}\n\t -Size : {self.size} \n"