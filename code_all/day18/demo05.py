"""
    lambda 应用
"""
from common.iterable_tools import IterableHelper

list01 = [342, 4, 54, 56, 6776]

# 定义函数,在列表中查找所有大于100的数
# def condition01(number):
#     return number > 100

# 定义函数,在列表中查找所有偶数
# def condition02(number):
#     return number % 2 == 0

for item in IterableHelper.find_all(list01,lambda number: number > 100):
    print(item)

for item in IterableHelper.find_all(list01,lambda number: number % 2 == 0):
    print(item)
