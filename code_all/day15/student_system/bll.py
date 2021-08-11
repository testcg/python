from typing import List

from model import StudentModel


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


if __name__ == '__main__':
    # 如果主模块才执行下面测试代码
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    for item in controller.students:
        print(item)
