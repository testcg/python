"""
    程序结构
        1. 主模块：第一次运行的模块
        2. 根目录：主模块所在文件夹
        3. 目录结构：
            项目根目录
            包(文件夹)
                模块(文件)
                    类
                        函数
                            语句
            main.py
"""
# 导入路径：从项目根目录开始

# 方式1：
# import 包.模块 as 别名
import package01.package02.module01 as m1

m1.func01()

# 方式2:
# from 包.模块 import 成员
from package01.package02.module01 import func01

func01()
