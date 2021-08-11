"""
    需求：
        定义函数，在员工列表中查找部门是9001的人数
        定义函数，在员工列表中查找薪资大于20000的人数
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(隔、做)
           创建通用函数get_count
        3. 在当前模块中使用lambda调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def get_count01():
    count = 0
    for emp in list_employees:
        if emp.did == 9001:
            count += 1
    return count


def get_count02():
    count = 0
    for emp in list_employees:
        if emp.money > 20000:
            count += 1
    return count


print(get_count01())


def get_count(condition):
    count = 0
    for emp in list_employees:
        # if emp.did == 9001:
        if condition(emp):
            count += 1
    return count
"""

print(IterableHelper.get_count(list_employees, lambda emp: emp.did == 9001))
print(IterableHelper.get_count(list_employees, lambda emp: emp.money > 20000))
