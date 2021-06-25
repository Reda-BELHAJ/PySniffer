import struct

class Icmp:
    def __init__(self, raw_data):
        self.icmp_type, self.code, self.checksum = struct.unpack('! B B H',raw_data[:4])
        self.data = raw_data[4:]
    
    def __str__(self) -> str:
        return f"\t -ICMP Type : {self.icmp_type}\n\t -ICMP Code :{self.code}\n\t -ICMP Checksum :{self.checksum}\n"