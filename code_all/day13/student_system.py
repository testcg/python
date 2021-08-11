"""
    学生管理系统

    练习：商品(名称,单价,编号)管理系统
        1. 添加商品信息
        2. 存储商品信息
"""


class StudentModel:
    """
        学生模型：封装数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid  # 学生全球唯一标识符


class StudentView:
    """
        学生视图:处理界面逻辑
    """

    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            # 先写方法调用,再alt+回车自动生成
            self.input_student()
        elif item == "2":
            pass

    def input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.score = int(input("请输入学生成绩："))
        stu.age = int(input("请输入学生年龄："))
        self.controller.add_employee(stu)
        print("添加成功")


class StudentController:
    """
        学生控制器：负责处理业务逻辑
    """

    start_id = 1000 # 类变量

    @classmethod # 类方法
    def set_student_id(cls, stu):
        stu.sid = cls.start_id
        cls.start_id += 1

    def __init__(self):
        self.students = []

    def add_student(self, stu):
        # stu.sid = StudentController.start_id
        # StudentController.start_id += 1
        StudentController.set_student_id(stu)
        self.students.append(stu)


controller = StudentController()
view = StudentView(controller)
while True:
    view.display_menu()
    view.select_menu()
