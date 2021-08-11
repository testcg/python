"""
    一家公司有如下几种岗位：
        程序员：底薪 + 分红
        测试员：底薪 + Bug数 × 5
        ....
        销售：底薪 + 销售额 × 0.03

    创建员工管理器
        -- 记录所有员工
        -- 提供计算总薪资的方法
"""


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.__employees.append(emp)

    def calculate_total_money(self):
        total_money = 0
        for item in self.__employees:
            total_money += item.get_money()
        return total_money


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_money(self):
        pass


class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_money(self):
        return self.base_salary + self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def get_money(self):
        return self.base_salary + self.bug_count * 5

manager = EmployeeManager()
manager.add_employee(Programmer(10000,500000))
manager.add_employee(Tester(6000,0))
print(manager.calculate_total_money())













