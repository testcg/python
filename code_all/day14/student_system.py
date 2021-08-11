"""
    学生管理系统

    练习：商品(名称,单价,编号)管理系统
        1. 添加商品信息
        2. 存储商品信息
        3. 封装现有代码,显示商品信息
        4. 删除商品信息
        5. 修改商品信息
"""

from typing import List


class StudentModel:
    """
        学生模型：封装数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid  # 学生全球唯一标识符

    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"

    # 相同依据
    def __eq__(self, other):
        return self.sid == other


class StudentView:
    """
        学生视图:处理界面逻辑
    """

    def __init__(self, controller):
        self.__controller = controller  # type:StudentController

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            # 先写方法调用,再alt+回车自动生成
            self.__input_student()
        elif item == "2":
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名：")
        stu.score = int(input("请输入学生成绩："))
        stu.age = int(input("请输入学生年龄："))
        self.__controller.add_student(stu)
        print("添加成功")

    def main(self):
        """
            入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        for stu in self.__controller.students:
            print(stu)

    def __delete_student(self):
        sid = int(input("请输入学生编号："))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.sid = int(input("请输入需要修改的学生编号："))
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = int(input("请输入需要修改的学生年龄："))
        stu.score = int(input("请输入需要修改的学生成绩："))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")


class StudentController:
    """
        学生控制器：负责处理业务逻辑
    """

    __start_id = 1000  # 类变量

    @classmethod  # 类方法
    def __set_student_id(cls, stu: StudentModel):
        stu.sid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__students = []  # type:List[StudentModel]

    @property
    def students(self):
        return self.__students

    def add_student(self, stu: StudentModel):
        """
            添加学生信息
        :param stu: StudentModel类型的新学生
        """
        # stu.sid = StudentController.start_id
        # StudentController.start_id += 1
        StudentController.__set_student_id(stu)
        self.__students.append(stu)

    def remove_student(self, sid: int) -> bool:
        """
            移除学生信息
        :param sid:int 类型的学生编号
        :return:是否删除成功
        """
        if sid in self.__students:
            self.__students.remove(sid)
            return True
        return False

    def update_student(self, stu: StudentModel) -> bool:
        for item in self.__students:
            if item.sid == stu.sid:
                # item.name = stu.name
                # item.age = stu.age
                # item.score = stu.score
                item.__dict__ = stu.__dict__
                return True
        return False


controller = StudentController()
view = StudentView(controller)
view.main()
