import os
from tkinter import messagebox
import time

def rename_file():
    file_path = r"D:/etcp_lts/lts"
    src_name_list = ["daemon_start.bat", "lts_start.bat"]
    file_list = os.listdir(file_path)
    for item in src_name_list:
        if item in file_list:
            os.rename(f"{file_path}/{item}", f"{file_path}/{item}1")
    alert()


def alert():
    title = "rename"
    message = "ζδ»Άζε"
    messagebox.showinfo(title, message, icon=None, type=None)


if __name__ == '__main__':
    rename_file()
    time.sleep(2)