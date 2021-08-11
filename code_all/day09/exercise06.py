"""
    练习：定义数值累乘的函数
"""


# 对于函数定义者而言,不定长参数意义不大(都是容器)
# 对于调用者而言,可以直接传递需要操作的多个数据(自动合并为容器)
def multiplicative(*args):
    result = 1
    for number in args:
        result *= number
    return result


print(multiplicative(342, 43, 54, 56, 67))

# def multiplicative(args):
#     result = 1
#     for number in args:
#         result *= number
#     return result
#
#
# print(multiplicative([342, 43, 54, 56, 67]))
