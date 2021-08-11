"""
    readlines([sizeint])
    功能： 读取文件中的每一行作为列表中的一项
    参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size表示读取到size字符所在行为止。
    返回值： 返回读取到的内容列表
"""
file = open('../file/file.txt', 'r')
print(file.readlines(5))

file.close()
