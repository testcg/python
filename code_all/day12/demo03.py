"""
    重写内置函数 - str
        改变其行为
"""
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 自定义对象 --> 字符串
    def __str__(self):
        return f"我叫{self.name},今年{self.age}岁了"

    # 自定义对象 --> int
    # def __int__(self):
    #     return self.age

wk = Person("悟空",26)
bj = Person("猪猪",23)
# <__main__.Person object at 0x7fac3a75fe48>
print(wk) #

message = bj.__str__() # str(bj)
print(message)

print(int(wk))