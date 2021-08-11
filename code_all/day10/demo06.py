"""
    小结 - Python语言所有变量
"""
# 全局变量:整个文件都可以使用
data01 = 10

def func01():
    # 局部变量:函数内部使用
    data02 = 20

class MyClass:
    # 类变量:通过类访问
    data04 = 40
    def __init__(self):
        # 实例变量:通过对象访问
        self.data03 = 30

m01 = MyClass()
print(m01.data03)
print(MyClass.data04)
