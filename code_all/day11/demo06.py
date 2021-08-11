"""
    属性各种写法
"""

# 写法1：读写属性
# 快捷键：props + 回车
class MyClass:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

m01 = MyClass(10)
m01.data = 20
print(m01.data)


# 写法2：只读属性
#  往往类中确定的数据,需要类外读取,但是不能修改
# 快捷键：prop + 回车
class MyClass:
    def __init__(self):
        # 私有变量
        self.__data = 10

    @property
    def data(self):
        return self.__data


m01 = MyClass()
# m01.data = 20# AttributeError: can't set attribute
print(m01.data)

# 写法3：只写属性
# 快捷键：无
class MyClass:
    def __init__(self, data=0):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        self.__data = value

m01 = MyClass(10)
m01.data = 20
# print(m01.data) # AttributeError: unreadable attribute
print(m01.__dict__)