"""
    属性property
        原理
            一个私有变量,两个公开方法
"""

"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.__age = age
        self.set_age(age)# 2

    def get_age(self):# 读取
        return self.__age

    def set_age(self,value):# 写入 3
        self.__age = value

ll = Wife("丽丽", 800)# 1
ll.set_age(20)
print(ll.get_age())
"""

"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        # self.set_age(age)

    def get_age(self):# 读取
        return self.__age

    def set_age(self,value):# 写入
        self.__age = value

    # 创建与实例变量名称相同的类变量
    age = property(get_age,set_age)


ll = Wife("丽丽", 800)#
# ll.set_age(20)
ll.age = 20 # ll.set_age(20)
# print(ll.get_age())
print(ll.age)
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property  # age = property(age)
    def age(self):
        return self.__age

    @age.setter  # age = age.setter(age)
    def age(self, value):
        self.__age = value


ll = Wife("丽丽", 800)
ll.age = 20
print(ll.age)
