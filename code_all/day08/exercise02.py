"""
    练习1： 定义函数,在终端中打印一维列表.
    list01 = [5, 546, 6, 56, 76, ]
    for item in list01:
        print(item)

    list02 = [7,6,879,9,909,]
    for item in list02:
    print(item)
"""


# 做(一种行为)
def print_single_list(list_target):
    """
        在终端中打印列表元素
    :param list_target: list类型的需要打印的数据
    """
    for item in list_target:
        print(item)


# 用(不同数据)
list01 = [5, 546, 6, 56, 76, ]
print_single_list(list01)

print_single_list([7, 6, 879, 9, 909, ])
