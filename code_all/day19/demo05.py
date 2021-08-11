"""
    装饰器 - 语法细节
        内函数返回值：旧功能的返回值
"""


def new_func(func):
    def wrapper(*args, **kwargs):  # 多合一
        print("新功能")
        result = func(*args, **kwargs)  # 一拆多
        return result

    return wrapper


@new_func
def func01(p1):
    print("旧功能1,参数:", p1)
    return 10


@new_func
def func02(p1, p2):
    print("旧功能2,参数:", p1, p2)
    return 20


# 调用内函数
print(func01(100))  # 10
print(func02(200, 300))  # 20
func02(p1=400, p2=500)
