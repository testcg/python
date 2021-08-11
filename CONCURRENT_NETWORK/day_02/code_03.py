"""
    tcp_server 循环
"""

from socket import *

tcp_server = socket()
tcp_server.bind(('0.0.0.0', 8888))
tcp_server.listen()
while True:
    connfd, addr = tcp_server.accept()
    data = connfd.recv(1024)
    print(f"来自客户端{addr}的消息：{data.decode()}")
    connfd.send(f"thanks".encode())
    connfd.close()
