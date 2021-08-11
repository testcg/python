"""
    udp_server
"""

from socket import *

# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定地址、端口
udp_socket.bind(('0.0.0.0', 8888))

"""
    功能： 接收UDP消息
    参数： 每次最多接收多少字节
    返回值： data  接收到的内容
            addr  消息发送方地址
"""
data, addr = udp_socket.recvfrom(1024 * 1024)
print(addr)
print(data.decode())  # 字节串收发
udp_socket.sendto(b'thanks', addr)
