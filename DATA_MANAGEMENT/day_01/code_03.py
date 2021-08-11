"""
    readline
    功能： 用来读取文件中一行
    参数： 如果没有给定size参数（默认值为-1）或者size值为负，表示读取一行，给定size表示最多读取制定的字符（字节）。
    返回值： 返回读取到的内容
"""
file = open('../file/file.txt', 'r')
while True:
    data = file.readline(1)
    if not data:
        break
    print(data, end='')

