class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# 练习1:定义函数,在员工列表中查找did是9001的所有员工
def find_employee_by_did():
    for item in list_employees:
        if item.did == 9001:
            yield item


# 调用函数不执行函数体，返回生成器对象(推算数据)
result = find_employee_by_did()
for item in result:
    print(item.__dict__)


# 练习2:定义函数,在员工列表中查找薪资大于20000的所有员工
def find_employee_by_money():
    for item in list_employees:
        if item.money > 20000:
            yield item


for emp in find_employee_by_money():
    print(emp.__dict__)


# 练习3:定义函数,在员工列表中查找eid是1003的员工
def find_employee_by_eid():
    for item in list_employees:
        if item.eid == 1003:
            return item


emp = find_employee_by_eid()
print(emp.__dict__)

# 缺点1：生成器对象只能使用(for)一次
# result = find_employee_by_money()
# for emp in result:
#     print(emp.__dict__)
# for emp in result: # 不执行
#     print(emp.__dict__)
# 缺点2：不能定位元素(不支持索引切片)
# print(result[-1])
# 解决：将生成器转换为容器
list_result = list(find_employee_by_money())


# 练习4:定义函数,在员工列表中查找所有员工的姓名
def find_employees_name():
    for item in list_employees:
        yield item.name


re = find_employees_name()
# for item in re:
#     print(item)
# for item in re:
#     print(item)
# print(re[0])
list_result = list(re)
print(list_result[0])
