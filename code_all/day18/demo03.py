"""
    函数式编程

"""
from common.iterable_tools import IterableHelper

list01 = [342, 4, 54, 56, 6776]

# 定义函数,在列表中查找所有大于100的数
def condition01(number):
    return number > 100

# 定义函数,在列表中查找所有偶数
def condition02(number):
    return number % 2 == 0

for item in IterableHelper.find_all(list01,condition01):
    print(item)













