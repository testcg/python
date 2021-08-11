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


# 定义函数,查找所有姓名小于三个字的学生
def find_students_by_name():
    for stu in list_student:
        if len(stu.name) < 3:
            yield stu


for item in find_students_by_name():
    print(item.__dict__)

students_by_name = (stu for stu in list_student if len(stu.name) < 3)
for item in students_by_name:
    print(item.__dict__)


# 定义函数,查找所有女同学
def find_students_by_sex():
    for stu in list_student:
        if stu.sex == "女":
            yield stu


# 延迟操作/惰性操作  -->  立即操作
list_student_by_sex = list(find_students_by_sex())
print(list_student_by_sex[-1].__dict__)

students_by_sex = (stu for stu in list_student if stu.sex == "女")


# 定义函数,查找所有成绩小于60的同学姓名
def get_student_names():
    for stu in list_student:
        if stu.score < 60:
            yield stu.name


student_names = (stu.name for stu in list_student if stu.score < 60)


# 定义函数,查找成绩最高的学生
def get_max_by_score():
    max_value = list_student[0]
    for i in range(1, len(list_student)):
        if max_value.score < list_student[i].score:
            max_value = list_student[i]
    return max_value
