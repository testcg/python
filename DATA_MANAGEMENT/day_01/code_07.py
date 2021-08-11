"""
    系统自动的在内存中为每一个正在使用的文件开辟一个空间，在对文件读写时都是先将文件内容加载到缓冲区，再进行读写。
    作用:
        1、减少和磁盘的交互次数，保护磁盘。
        2、提高了对文件的读写效率。
"""
"""
    刷新缓冲区条件
        1、缓冲区被写满
        2、程序执行结束或者文件对象被关闭
        3、程序中调用flush()函数
"""


def buffer_01():
    file = open("../file/file_202107050946.txt", 'a+', encoding="utf-8")
    while True:
        data = input(">>")
        if not data:
            break
        file.write(f"{data}")
        file.flush()  # 调用flush函数时，刷新缓冲区
    file.close()


def buffer_02():
    # buffering=1时，遇到"\n"时刷新缓冲
    file = open("../file/file_202107050947.txt", 'w+', encoding="utf-8", buffering=1)
    while True:
        data = input(">>")
        if not data:
            break
        file.write(f"{data}\n")
    file.close()


def buffer_03():
    # buffering > 1,必须以二进制方式打开,指定缓冲区的大小
    file = open("../file/file_202107050948.txt", 'wb', buffering=10)
    while True:
        data = input(">>")
        if not data:
            break
        file.write(data.encode())
    file.close()

buffer_03()