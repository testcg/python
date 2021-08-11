"""
    yield
"""


class StudentController:
    """
        学生可迭代对象
    """

    def __init__(self):
        self.__students = []

    def add_student(self, stu):
        self.__students.append(stu)

    def __iter__(self):
        # 生成代码的大致规则：
        # 1. 将yield关键字前面的代码作为__next__函数体
        # 2. 将yield关键字后面的数据作为__next__返回值
        index = 0
        yield self.__students[index]

        index += 1
        yield self.__students[index]

        index += 1
        yield self.__students[index]


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
