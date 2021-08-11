""""
    继承 - 数据
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# class Student(Person):
#     pass

# 1. 子类若没有构造函数,直接使用父类.
# s = Student("悟空",26)

# 2. 子类有构造函数,覆盖父类(好像父类不存在构造函数)
class Student(Person):
    # 3. 子类构造函数参数:父类 + 子类
    def __init__(self, name="", age=0, score=0):
        # super() 通过父类调用构造函数
        super().__init__(name, age)
        self.score = score


s = Student("悟空", 26, 100)
print(s.name)
