"""
   练习2：定义函数，将列表中大于某个值的元素设置为None
             参数                           结果
   [34, 545, 56, 7, 78, 8]  -10->  [None,None,None,7,None,8]
   [34, 545, 56, 7, 78, 8]  -100->  [34, None, 56, 7, 78, 8]
"""


def set_none_gt_value(data, value):
    """
        将列表中大于某个值的元素设置为None
    :param data: 列表
    :param value: 值
    """
    for i in range(len(data)):
        if data[i] > value:
            # 修改可变数据
            data[i] = None

list01 = [34, 545, 56, 7, 78, 8]
set_none_gt_value(list01, 10)
print(list01)

list01 = [34, 545, 56, 7, 78, 8]
set_none_gt_value(list01, 100)
print(list01)
