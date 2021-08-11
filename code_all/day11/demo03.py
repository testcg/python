"""
    私有成员
        语法：以双下划线命名
        作用：类外无法访问
        本质：障眼法
            看上去双下划线命名,实际上是单下划线+类名+双下划线
                 __data     _MyClass__data
"""


class MyClass:
    def __init__(self, data=0):
        self.__data = data

    def __func01(self):
        print("func01执行了")

    def func02(self):
        print(self.__data)


m01 = MyClass()
print(m01._MyClass__data)
print(m01.__dict__)
# print(m01.__data)
# m01.__func01()
m01._MyClass__func01()
