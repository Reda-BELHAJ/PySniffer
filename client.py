import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(10):
    message = b'{str(i)}fada awfasfwa afewfasf awf'
    s.sendto(message, ('127.0.0.1', 9999))