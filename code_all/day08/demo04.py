"""
    函数 - 返回值
        创建函数 给 调用函数传递的结果
"""


# 需求：定义函数,两个数字相加
# def add():
#     number_one = int(input("请输入第一个数字："))
#     number_two = int(input("请输入第二个数字："))
#     result = number_one + number_two
#     print("结果是：%s" % result)
#
# add()

# def add(number_one,number_two):
#     result = number_one + number_two
#     print("结果是：%s" % result)
#
# add(15,20)

def add(number_one, number_two):
    result = number_one + number_two
    return result  # 返回数据


re = add(15, 20)
print("结果是：%s" % re)
