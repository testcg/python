"""
    tcp_client 循环
"""

from socket import *
while True:
    tcp_client = socket()
    server_addr = ('10.44.111.135', 8888)
    msg = input(">>")
    if not msg:
        break
    tcp_client.connect(server_addr)
    tcp_client.send(msg.encode())
    data = tcp_client.recv(1024)
    print(f"来自服务端的消息：{data.decode()}")
    tcp_client.close()


"01:36:59"