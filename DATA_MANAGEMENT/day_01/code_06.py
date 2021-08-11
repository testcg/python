"""
    python中的with语句也可以用于访问文件，在语句块结束后会自动释放资源。
"""
with open("../file/file_01.txt", "a+") as f:
    f.write("hello world!\n")
    data = f.read()
    print(data)

