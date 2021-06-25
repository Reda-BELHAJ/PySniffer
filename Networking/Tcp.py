import struct

class Tcp:
    def __init__(self, raw_data):
        (self.src_port, self.dest_port, self.sequence, self.acknowledgment, offset_reserved_flags) = struct.unpack(
            '! H H L L H', raw_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.flag_urg = (offset_reserved_flags & 32) >> 5
        self.flag_ack = (offset_reserved_flags & 16) >> 4
        self.flag_psh = (offset_reserved_flags & 8) >> 3
        self.flag_rst = (offset_reserved_flags & 4) >> 2
        self.flag_syn = (offset_reserved_flags & 2) >> 1
        self.flag_fin = offset_reserved_flags & 1
        self.data = raw_data[offset:]

    def __str__(self) -> str:
        return f"\t -Source Port : {self.src_port}\n\t -Destination Port : {self.src_port}\n\t -Sequence : {self.sequence}\n\t -Acknowledgment : {self.acknowledgment}\n"

    def show_flags(self) -> str:
        return f"\t -Flags Urg :{self.flag_urg}\n\t\t -Ack : {self.flag_ack}\n\t\t -Psh : {self.flag_psh}\n\t\t -Rst : {self.flag_rst}\n\t\t -Syn : {self.flag_syn}\n\t\t -Fin : {self.flag_fin}\n"