"""
    tcp_client
"""

from socket import *

# 创建tcp套接字
tcp_client = socket()
# tcp连接服务端
server_addr = ('10.44.111.135', 8888)
tcp_client.connect(server_addr)
while True:
    data = input(">>")
    tcp_client.send(data.encode())
    # 如果输入##关闭客户端
    if data == '##':
        break
    recv_data = tcp_client.recv(1024)
    print(recv_data.decode())
tcp_client.close()
