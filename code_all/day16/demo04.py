"""
    迭代器
"""


# 声明：下列代码主要用于学习创建迭代器
class StudentIterator:
    """
        学生迭代器
    """
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index == len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class StudentController:
    """
        学生可迭代对象
    """
    def __init__(self):
        self.__students = []

    def add_student(self, stu):
        self.__students.append(stu)

    def __iter__(self):
        return StudentIterator(self.__students)


controller = StudentController()
controller.add_student("郭世鑫")
controller.add_student("刘兰涛")
controller.add_student("穆东宇")

# for item in controller:
#     print(item) #
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  #
    except StopIteration:
        break
