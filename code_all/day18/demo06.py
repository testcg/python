"""
    内置高阶函数
"""


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

# 1. map 映射
# 需求:获取所有员工姓名
for item in map(lambda item: item.name, list_employees):
    print(item)

# 2. filter 过滤器
# 需求：查找所有部门是9002的员工
for item in filter(lambda item: item.did == 9002, list_employees):
    print(item.__dict__)

# 3. max min 最值
emp = max(list_employees, key=lambda emp: emp.money)
print(emp.__dict__)

# 4. sorted
# 升序排列
new_list = sorted(list_employees, key=lambda emp: emp.money)
print(new_list)
# 降序排列
new_list = sorted(list_employees, key=lambda emp: emp.money, reverse=True)
print(new_list)
