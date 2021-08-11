"""
    复习
        跨类调用
            行为不同用类区分
            数据不同用对象区分
            方法1:
            class A:
                def func01():
                    b = B()
                    b.func02()

            class B:
                def func02():
                    ...

            方法2:
            class A:
                def __init__(self):
                    self.b = B()

                def func01():
                    b.func02()

            class B:
                def func02():
                    ...

            方法3:
            class A:
                def func01(obj):
                    obj.func02()

            class B:
                def func02():
                    ...

            a = A()
            a.func01(B())
            a.func01(C())

        属性
            保护数据有效范围
            语法：
            class A:
                def __init__(self,data):
                    self.data = data

                @property
                def data(self): # 读取
                    return self.__data

                @data.setter
                def data(self,value): 写入
                    self.__data = value

            a = A(10):
            print(a.data)


"""