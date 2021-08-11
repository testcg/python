"""
    练习：使用tcp完成。将一个图片从客户端发送到服务端
"""

from socket import *
from time import sleep

tcp_server = socket()
tcp_server.bind(('0.0.0.0', 8888))
tcp_server.listen()
connfd, addr = tcp_server.accept()
print(f"{addr}已连接")
data_name = connfd.recv(1024).decode()
print(data_name)
# file = open(f"pic/互联网支付设备异常.png", 'wb+')
file = open(f"./{data_name}", 'wb+')
connfd.send('1000'.encode())
while True:
    data = connfd.recv(1024)
    if data == b'1001':
        file.close()
        print(f"接收完成")
        break
    file.write(data)
connfd.send(f"上传成功".encode())
sleep(2)
connfd.close()
tcp_server.close()
