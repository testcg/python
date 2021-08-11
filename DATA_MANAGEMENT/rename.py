import getpass
import os
from time import sleep

import pythoncom
from win32comext.shell import shell


# 重命名文件
def rename_file():
    file_path = r"D:/etcp_lts/lts"
    src_name_list = ["daemon_start.bat", "lts_start.bat"]
    file_list = os.listdir(file_path)
    for item in src_name_list:
        if item in file_list:
            os.rename(f"{file_path}/{item}", f"{file_path}/{item}1")
            sleep(1)
            print(f"{item} file rename  ok")
    print(f"all files rename ok")


# 获取当前用户名
def get_user():
    return getpass.getuser()


def remove_start(file_path: str):
    file_list = os.listdir(file_path)
    for item in file_list:
        os.remove(f"{file_path}/{item}")


def set_shortcut(filename, lnkname):
    shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
    shortcut.SetPath(filename)

    shortcut.SetWorkingDirectory(r"D:/gsglsf")  # 设置快捷方式的起始位置, 不然会出现找不到辅助文件的情况
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)
    print("add startup OK")


def is_seven_or_ten():
    path = rf"C:\Users"
    dir_list = os.listdir(path)
    if "user" in dir_list and "Administrator" not in dir_list:
        return rf"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    elif "user" not in dir_list and "Administrator" in dir_list:
        return rf"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    else:
        print("file not exist")
        return None


if __name__ == '__main__':
    rename_file()
    start_file_path = is_seven_or_ten()
    if start_file_path:
        remove_start(start_file_path)
        set_shortcut(r"D:/gsglsf/daemon.vbs",
                     rf"{start_file_path}/daemon.vbs.lnk")

