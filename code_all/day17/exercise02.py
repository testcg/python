"""
    练习2. 定义函数,在列表中找出所有数字
    [43,"悟空",True,56,"八戒",87.5,98]
"""


# 适用性
# 函数有一个结果使用return
# 函数有多个结果使用yield
def get_number1(list_number):
    result = []
    for item in list_number:
        if type(item) in (int, float):
            result.append(item)
    return result


def get_number2(list_number):
    for item in list_number:
        if type(item) in (int, float):
            yield item


list01 = [43, "悟空", True, 56, "八戒", 87.5, 98]
for item in get_number1(list01):
    print(item)

for item in get_number2(list01):
    print(item)
