"""
    TCP_server
    练习：客户端退出后，服务端不退出，可以处理下一个客户端
"""
from socket import *

# 创建TCP套接字
socked = socket()
# 绑定地址，端口
socked.bind(('0.0.0.0', 8888))
# 设置监听
socked.listen(10)
# 等待客户端连接
while True:
    print(f"waiting connect......")
    connfd, addr = socked.accept()
    print(f"{addr} having connect")
    while True:
        data = connfd.recv(1024)
        if not data.decode() or data.decode() == '##':
            print(f"{addr}客户端已断开连接")
            break
        print(data.decode())
        n = connfd.send('hi'.encode())
    connfd.close()
