import struct

def ipv4(addr):
        return ".".join(map(str, addr))

class Ipv4:
    def __init__(self, raw_data):
        version_header_lenght = raw_data[0]

        self.version = version_header_lenght >> 4
        self.header_lenght = (version_header_lenght & 15) * 4

        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])

        self.src, self.target = ipv4(src), ipv4(target)

        self.data = raw_data[20:]