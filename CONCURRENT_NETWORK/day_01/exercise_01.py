"""
    客户端循环输入，服务端循环输出，客户端直接回车，客户端结束输入
"""
from socket import *


def socked_server():
    udp_socked = socket(AF_INET, SOCK_DGRAM)
    udp_socked.bind(('0.0.0.0', 8888))
    while True:
        data, addr = udp_socked.recvfrom(1024)
        print(data.decode())
        print(addr)
        udp_socked.sendto(b'thanks', addr)


def socked_client():
    udp_socked = socket(AF_INET, SOCK_DGRAM)
    server_addr = ('121.5.59.138', 8888)
    while True:
        data = input(">>")
        if not data:
            udp_socked.close()
            break
        udp_socked.sendto(data.encode(), server_addr)
        data_rec, addr = udp_socked.recvfrom(1024)
        print(data_rec.decode())


if __name__ == '__main__':
    socked_client()
