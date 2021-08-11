"""
    编写一个函数，传入一个具体文件，将传入的文件以当前日期为名字，拷贝到当前文件夹
"""
import time


def copy(file_path: str):
    file_read = open(file_path, 'rb')
    file_write = open(f"../../file/{get_time()}.{file_path.split('.')[-1]}", "wb+")

    while True:
        # 不进行一次性读取，循环读取,每次读取4M，直到读取完毕
        data = file_read.read(1024 * 1024 * 4)
        file_write.write(data)
        if not data:
            break
    file_read.close()
    file_write.close()


def get_time():
    now_time = time.localtime()
    str_time = time.strftime("%Y%m%d%H%M%S", now_time)
    return str_time


file_01 = "../../file/互联网支付设备异常.png"
file_02 = "../../file/file_01.txt"


# copy(file_03)
