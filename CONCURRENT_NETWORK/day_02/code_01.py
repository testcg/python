"""
    TCP_server
"""
from socket import *

# 创建TCP套接字
socked = socket()
# 绑定地址，端口
socked.bind(('0.0.0.0', 8888))
# 设置监听
socked.listen(10)
# 等待客户端连接
print(f"waiting connect......")
connfd, addr = socked.accept()
print(f"{addr} having connect")
while True:
    data = connfd.recv(1024)
    if data.decode() == '##':
        connfd.close()
        print(f"{addr}客户端已断开连接，服务端关闭")
        break
    print(data.decode())
    n = connfd.send('hi'.encode())
connfd.close()
socked.close()