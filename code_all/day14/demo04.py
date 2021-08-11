"""

"""
# 标记项目根目录：
# 在文件夹上右键 --> Mark Driectory --> Source Root

# 导入方式1:
# "我过去"
# import 模块名
# 模块名.成员
import module01

module01.func01()

# 导入方式2:
# "你过来"
# from 模块 import 成员
# 直接使用
# 注意：导入的成员命名冲突
# from module01 import func01,func02
from module01 import *

def func01():
    print("demo01 - func01")

func01()
func02()
