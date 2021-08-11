"""
    定义函数,在列表中获取最小值
    list01 = [170, 160, 180, 165]
    min_value = list01[0]
    for i in range(1, len(list01)):
        if min_value > list01[i]:
            min_value = list01[i]
    print(min_value)
"""


def get_min(list_target):
    # 2.没有修改可变数据,所以结果必须通过return返回
    min_value = list_target[0]
    for i in range(1, len(list_target)):
        if min_value > list_target[i]:
            min_value = list_target[i]
    return min_value


# 1. 传入可变数据
list01 = [170, 160, 180, 165]
res = get_min(list01)
print(res)
