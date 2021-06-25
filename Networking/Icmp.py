import struct

class Icmp:
    def __init__(self, raw_data):
        self.icmp_type, self.code, self.checksum = struct.unpack('! B B H',raw_data[:4])
        self.data = raw_data[4:]