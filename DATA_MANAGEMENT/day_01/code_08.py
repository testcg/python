"""
    打开一个文件进行操作时系统会自动生成一个记录，记录每次读写操作时所处的文件位置，每次文件的读写操作都是从这个位置开始进行的。
    注意：
        1、r或者w方式打开，文件偏移量在文件开始位置
        2、a方式打开，文件偏移量在文件结尾位置
"""

"""
    tell()
        功能：获取文件偏移量大小
        返回值：文件偏移量
    seek(offset[,whence])
        功能: 移动文件偏移量位置
        参数：offset  代表相对于某个位置移动的字节数。负数表示向前移动，正数表示向后移动。
             whence是基准位置的默认值为 0，代表从文件开头算起，1代表从当前位置算起，2 代表从文件末尾算起。
            注意：必须以二进制方式打开文件时，基准位置才能是1或者2
"""
def file_seek():
    file = open("../file/file_2021007051034.txt", "wb+")
    while True:
        data_input = input(">>")
        if not data_input:
            break
        file.write(data_input.encode())
        file.flush()
    print(f"文件偏移量为{file.tell()}")
    file.seek(0 - file.tell(), 1)
    data_output = file.read().decode()
    print(data_output)
