from socket import *
from time import sleep

tcp_client = socket()
# addr = ('121.5.59.138', 8888)
addr = ('10.44.111.135', 8888)
tcp_client.connect(addr)
path = "../../DATA_MANAGEMENT/file"
file_name = "互联网支付设备异常.png"
file = open(f"{path}/{file_name}", 'rb')
tcp_client.send(file_name.encode())
print(tcp_client.recv(1024).decode())
while True:
    data = file.read(1024)
    if not data:
        file.close()
        tcp_client.send(f"1001".encode())
        print(f"1001传输完成")
        break
    tcp_client.send(data)
recv_data = tcp_client.recv(1024)
print(recv_data.decode())
tcp_client.close()
