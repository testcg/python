"""
    导入包
"""
# 方式1:import 包 as 别名
# 需要在包的__init__.py文件中指定需要访问的成员
# import package01.package02 as p
#
# p.module01.func01()
#
# p.func01()

# 方式2:from 包.包 import 成员
from package01.package02 import module01,func01

module01.func01()
func01()

