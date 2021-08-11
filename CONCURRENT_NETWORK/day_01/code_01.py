import socket

# 创建一个UDP套接字
socked = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 参数： 二元元组 (ip,port)  绑定本机网络地址
socked.bind(('0.0.0.0', 10000))

# 发送UDP消息
data = 'hello'
socked.sendto(data.encode(), ('10.44.111.135', 60000))
