class EmployeeModel:
    """
        员工模型
    """

    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class EmployeeView:
    """
        员工视图:处理界面逻辑
    """

    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("按1键录入员工信息")
        print("按2键显示员工信息")
        print("按3键删除员工信息")
        print("按4键修改员工信息")

    def select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.input_employee()
        elif item == "2":
            pass

    def input_employee(self):
        emp = EmployeeModel()
        emp.name = input("请输入员工姓名：")
        emp.did = int(input("请输入部门编号："))
        emp.money = int(input("请输入员工薪资："))
        self.controller.add_employee(emp)
        print("添加成功")


class EmployeeController:
    """
        员工控制器：负责处理业务逻辑
    """

    start_id = 1000

    @classmethod
    def set_employee_id(cls, emp):
        emp.eid = cls.start_id
        cls.start_id += 1

    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        EmployeeController.set_employee_id(emp)
        self.employees.append(emp)


controller = EmployeeController()
view = EmployeeView(controller)
while True:
    view.display_menu()
    view.select_menu()
