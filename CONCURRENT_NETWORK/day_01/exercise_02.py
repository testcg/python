"""
    客户端输入单词，服务端返回单词解释
"""
# coding=utf8
from socket import *


def socket_server():
    udp_socked = socket(AF_INET, SOCK_DGRAM)
    udp_socked.bind(('0.0.0.0', 8888))
    while True:
        data, addr = udp_socked.recvfrom(1024)
        print(data.decode())
        result = query_word(data.decode())
        if not result:
            udp_socked.sendto('this word input error, query result is null'.encode(), addr)
            continue
        udp_socked.sendto(result.encode(), addr)


def query_word(word):
    file = open('dict.txt', 'r')
    for item in file:
        item_ = item.split(' ', 1)
        if word == item_[0]:
            return item_[1].strip()
    return None


def socked_client():
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


if __name__ == '__main__':
    socket_server()
