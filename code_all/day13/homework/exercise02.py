"""　
    定义函数,根据员工编号,删除员工信息,返回是否删除成功
"""


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __eq__(self, other):
        return self.eid == other


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def delete_employee(cid):
    """
       定义函数,根据员工编号,删除员工信息,返回是否删除成功
    :param cid: 需要删除的员工编号
    :return: 是否删除成功
    """
    if cid in list_employees:
        list_employees.remove(cid)
        return True
    return False


print(delete_employee(1005))  # True
print(list_employees)
