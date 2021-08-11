"""
    read([size])
    功能： 来直接读取文件中字符。
    参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size最多读取给定数目个字符（字节）。
    返回值： 返回读取到的内容
"""
# open打开一个文件
# file = open("../file/file.txt", 'r')  # 以读方式打开，文件必须存在
# file = open("../file/file.txt", 'w') # 	以写方式打开，文件不存在则创建，存在清空原有内容
# file = open("../file/file.txt", 'a')  # 以追加模式打开，文件不存在则创建，存在则继续进行写操作
file = open("../file/file.txt", 'r')
# data = file.read()
# print(data)
# file.close()  # 关闭读取文件
# 循环读取文件
while True:
    # 文件读取完，会返回一个空字符串
    data = file.read(2)
    if not data:
        break
    print(data, end='')
