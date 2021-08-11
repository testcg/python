"""
    编写一个函数，传入一个文件夹，删除该文件夹中小于100kb的文件
"""
import os


def delete_file(dir):
    file_list = os.listdir(dir)
    for file in file_list:
        filename = f"{dir}/{file}"
        size = os.path.getsize(filename)
        if size < 1024 * 100 and os.path.isfile(filename):
            os.remove(filename)


delete_file("../../test_file")
