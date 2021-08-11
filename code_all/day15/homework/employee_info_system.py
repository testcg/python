"""
    信息管理系统
"""

#            架构
# 迎宾 - 服务员 - 厨师 - 配菜员
from typing import List


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class EmployeeView:
    """
        商品信息视图
    """

    def __init__(self, controller):
        self.__controller = controller  # type:EmployeeController

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1 添加员工")
        print("2 显示员工")
        print("3 删除员工")
        print("4 修改员工")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_employee()
        elif item == "2":
            self.__display_employees()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__modify_employee()

    def __input_employee(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))
        self.__controller.add_employee(employee)

    def __display_employees(self):
        for item in self.__controller.all_employee:
            print(item.__dict__)

    def __delete_employee(self):
        cid = int(input("请输入员工编号："))
        if self.__controller.remove_employee(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee = EmployeeModel()
        employee.eid = int(input("请输入员工编号："))
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))

        if self.__controller.update_employee(employee):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController:
    """
        商品信息控制器
    """
    __start_id = 1001

    @classmethod
    def __set_employee_id(cls, emp):
        emp.eid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__all_employee = []  # type:List[EmployeeModel]
        self.__start_eid = 1001

    @property
    def all_employee(self):
        return self.__all_employee

    def add_employee(self, emp: EmployeeModel):
        """
            添加商品信息
        :param employee:需要添加的商品信息
        """
        EmployeeController.__set_employee_id(emp)
        self.__all_employee.append(emp)

    def remove_employee(self, eid: int) -> bool:
        """
            根据商品编号删除商品信息
        :param cid:商品编号
        :return:是否删除成功
        """
        for i in range(len(self.__all_employee)):
            if self.__all_employee[i].eid == eid:
                del self.__all_employee[i]
                return True
        return False

    def update_employee(self, commodity: EmployeeModel) -> bool:
        """
            修改商品信息
        :param commodity:商品信息
        :return:是否删除成功
        """
        for item in self.__all_employee:
            if item.eid == commodity.eid:
                item.__dict__ = commodity.__dict__
                return True
        return False


view = EmployeeView(EmployeeController())
view.main()
