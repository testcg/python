"""
    获取文件大小
    os.path.getsize(file)
    功能： 获取文件大小
    参数： 指定文件
    返回值： 文件大小
"""
import os

# 获取文件大小
print(os.path.getsize("../file/new_file.txt"))

"""
    查看文件列表
    os.listdir(dir)
    功能： 查看文件列表
    参数： 指定目录
    返回值：目录中的文件名列表
"""
# 查看文件列表
print(os.listdir("../"))

"""
    查看文件是否存在
    os.path.exists(file)
    功能： 查看文件是否存在 
    参数： 指定文件
    返回值：存在返回True，不存在返回False
"""
# 判断文件是否存在
print(os.path.exists("../file/new_file.txt"))

"""
    判断文件类型
    os.path.isfile(file)
    功能： 判断文件类型 
    参数： 指定文件
    返回值：普通文件返回True，否则返回False
"""
# 判断是否为普通文件，如果是文件，返回true，如果是文件夹，返回false
print(os.path.isfile("."))

"""
    删除文件
    os.remove(file)
    功能： 删除文件 
    参数： 指定文件
"""
# os.remove("../file/file.txt")
