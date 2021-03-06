"""
    练习：使用学生列表封装以下三个列表中数据
    list_student_name = ["悟空", "八戒", "白骨精"]
    list_student_age = [28, 25, 36]
    list_student_sex = ["男", "男", "女"]
"""


class Student:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex


# list_student_name = ["悟空", "八戒", "白骨精"]
# list_student_age = [28, 25, 36]
# list_student_sex = ["男", "男", "女"]
# list_student = []
# for data in zip(list_student_name, list_student_age, list_student_sex):
#     stu = Student(data[0],data[1],data[2])
#     list_student.append(stu)
# print(list_student)

list_datas = [
    ["悟空", "八戒", "白骨精"],
    [28, 25, 36],
    ["男", "男", "女"]
]
# list_student = []
# for data in zip(*list_datas):
#     stu = Student(*data)
#     list_student.append(stu)
list_student = [Student(*data) for data in zip(*list_datas)]
print(list_student)
