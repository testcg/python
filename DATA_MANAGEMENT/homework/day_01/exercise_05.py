"""
    编写一个程序，将两个文件合并为一个文件
"""


def merge_file(file_list: list):
    file_format = file_list[0].split('.')[-1]
    # for file_ in file_list:
    #     if file_.split('.')[-1] != file_format:
    #         print("文件格式不一致，不进行合并")
    #         return False
    file_new = open(f"../../file/new_file.{file_format}", "wb")
    for item in file_list:
        file = open(item, "rb")
        while True:
            data = file.read(1024 * 1024 * 4)
            if not data:
                break
            file_new.write(data)
        file.close()


file_list_ = ["../../file/file.txt", "../../file/file_01.txt"]
merge_file(file_list_)
