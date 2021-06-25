import struct

class Ipv4:
    def __init__(self, raw_data):
        version_header_lenght = raw_data[0]

        self.version = version_header_lenght >> 4
        self.header_lenght = (version_header_lenght & 15) * 4

        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])

        self.src, self.target = self.ipv4(src), self.ipv4(target)

        self.data = raw_data[20:]
    
    def ipv4(self, addr):
        return ".".join(map(str, addr))

    def __str__(self) -> str:
        return f"\t Version : {self.version}\n\t Header_lenght :{self.header_lenght}\n\t TTL : {self.ttl}\n\t Prototype : {self.proto}\n\t Source : {self.src}\n\t Target : {self.target}\n"