"""
    写一个程序，向一个文件当中不断写入内容，每隔两秒写一次,当程序重新启动后，继续写入，序号能够衔接
    1.2021-07-07  10:54:00
    2.2021-07-07  10:54:02
    3.2021-07-07  10:54:04
    ...
"""
import time


def write_log():
    file = open("../../file/my_log.log", "ab+")
    file.seek(0, 0)  # 文件偏移量置于开头
    num = len(file.readlines()) + 1  # 序号=行数+1
    while True:
        data = f"{num}.{get_time()}\n"
        file.write(data.encode())
        file.flush()
        time.sleep(2)
        num += 1


def get_time():
    now_time = time.localtime()
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", now_time)
    return str_time


write_log()
