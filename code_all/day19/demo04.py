"""
    装饰器
        在不改变旧功能基础上,增加新功能
        核心逻辑：
            拦截调用
"""

"""
def func01():
    print("旧功能")


def new_func():
    print("新功能")
"""

"""
def func01():
    print("旧功能")


def new_func(func):  # 得旧功能
    def wrapper():  # 用新旧功能
        print("新功能")
        func()

    return wrapper


# 新功能覆盖了旧功能
# func01 = new_func

# 调用一次外部函数
func01 = new_func(func01)
# 调用多次内部函数
func01()
func01()
"""


def new_func(func):  # 得旧功能
    def wrapper():  # 用新旧功能
        print("新功能")
        func()  # 3.执行旧功能

    return wrapper


# 1.调用外部函数
@new_func  # func01 = new_func(func01)
def func01():
    print("旧功能")


# 2.调用内部函数
func01()
func01()
