"""
    练习1：
    需求：
        定义函数，在列表中查找奇数
        定义函数，在列表中查找能被3或5整除的数字
    步骤：
            1. 根据需求，写出函数。
            2. 因为主体逻辑相同,核心算法不同.
               所以使用函数式编程思想(分、隔、做)
               创建通用函数find_all
            3. 在当前模块中调用
"""
list01 = [43, 54, 56, 76, 8]


def get_odd():
    for number in list01:
        if number % 2:
            yield number


def get_number():
    for number in list01:
        if number % 3 == 0 or number % 5 == 0:
            yield number


# 1.分
# 1.1 变化点函数
def condition01(number):
    return number % 2


def condition02(number):
    return number % 3 == 0 or number % 5 == 0


# 1.2 通用函数
# 2 隔
# 2.1 抽象为参数
def find_all(condition):
    for number in list01:
        # if number % 3 == 0 or number % 5 ==0:
        # if condition01(number):
        # if condition02(number):
        if condition(number):  # 2.2 统一调用方式
            yield number


# 3 做
# 3.1 新变化点
def condition03(num):
    return num < 10


# 3.2 执行
for item in find_all(condition02):
    print(item)
