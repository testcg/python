"""
    udp_client
"""
from socket import *

udp_socked = socket(AF_INET, SOCK_DGRAM)
server_addr = ('10.44.111.135', 8888)
while True:
    data = input(">>")
    if not data:
        udp_socked.close()
        break
    udp_socked.sendto(data.encode(), server_addr)
    data_rec, addr = udp_socked.recvfrom(1024)
    print(data_rec.decode())
