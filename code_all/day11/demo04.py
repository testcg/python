"""
    属性
        价值：保护数据在有效范围内
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age  # 藏

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            raise Exception("我不要")


ll = Wife("丽丽", 38)
print(ll.name)
print(ll.age)
