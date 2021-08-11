"""
    1. 使用lambda完成下列功能
    2. 在新模块中调用,实现以下功能:
            -- 在数字列表中查找奇数
            -- 在数字列表中查找能被3或5整除的数字

            -- 在学生列表查找所有姓名小于三个字的学生
            -- 在学生列表查找所有女同学
"""
from common.iterable_tools import IterableHelper


class Student:
    def __init__(self, name="", age=0, score=0, sex=""):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex


list_student = [
    Student("悟空", 26, 96, "男"),
    Student("八戒", 25, 50, "男"),
    Student("唐僧", 23, 53, "女"),
    Student("小白龙", 29, 85, "女"),
]

list01 = [43, 54, 56, 76, 8]

for item in IterableHelper.find_all(list01, lambda number: number % 2):
    print(item)

for item in IterableHelper.find_all(list01, lambda number: number % 3 == 0 or number % 5 == 0):
    print(item)

for stu in IterableHelper.find_all(list_student, lambda item: len(item.name) < 3):
    print(stu.__dict__)

for stu in IterableHelper.find_all(list_student, lambda item: item.sex == "女"):
    print(stu.__dict__)
