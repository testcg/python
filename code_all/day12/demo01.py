"""
    继承 - 行为
        财产：钱不用孩子挣,但是可以直接花
        皇位：江山不用太子打,但是可以直接坐
        编程：代码不用子类写,但是可以直接用
"""
# 在生活中,先有父再有子,存在"不劳而获的快感".

# 在程序中,从设计角度讲,先有子类再有父类
# 多个类型,有代码的共性,且都属于一种概念.
#           编码    ,先有父类再有子类
"""
class Teacher:
    def say(self):
        print("说话")

    def teach(self):
        print("教学")

class Student:
    def say(self):
        print("说话")

    def study(self):
        print("学习")
"""


class Person:
    def say(self):
        print("说话")


class Teacher(Person):
    def teach(self):
        self.say()
        print("教学")


class Student(Person):
    def study(self):
        print("学习")


# 创建父类对象,只能访问父类成员
p = Person()
p.say()

# 创建子类对象
t = Teacher()
t.say()
t.teach()

s = Student()
s.say()
s.study()

# 关系判断
# 人对象 是一种 人类型
print(isinstance(p, Person))  # True
# 老师对象 是一种 人类型
print(isinstance(t, Person))  # True
# 人对象 是一种 老师类型
print(isinstance(p, Teacher))  # False
# 学生对象 是一种 老师类型
print(isinstance(s, Teacher))  # False

# 人类型 是一种 人类型
print(issubclass(Person, Person))  # True
# 老师类型 是一种 人类型
print(issubclass(Teacher, Person))  # True
# 人类型 是一种 老师类型
print(issubclass(Person, Teacher))  # False
# 学生类型 是一种 老师类型
print(issubclass(Student, Teacher))  # False

# 人对象的类型 是 人类型
print(type(p) == Person)  # True
# 老师对象的类型 是 人类型
print(type(t) == Person)  # False
# 人对象的类型 是 老师类型
print(type(p) == Teacher)  # False
# 学生对象的类型 是 老师类型
print(type(s) == Teacher)  # False
