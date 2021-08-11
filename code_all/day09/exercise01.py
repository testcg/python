"""
    练习1：定义函数，根据值对字典进行升序排列
        提示：字典 --> 列表
             列表 --> 字典
"""


def sort_for_dict(target):
    """
        对字典进行升序排列
    :param target:目标字典
    :return:排好序的新字典
    """
    # [(1001, 10000), (1002, 10000)]
    list_data = list(target.items())
    for r in range(len(list_data) - 1):
        for c in range(r + 1, len(list_data)):
            if list_data[r][1] > list_data[c][1]:
                # 修改新数据
                list_data[r], list_data[c] = list_data[c], list_data[r]
    return dict(list_data)


commoditys = {
    1001: 10000,
    1002: 10000,
    1003: 52100,
    1004: 20,
    1005: 30,
}

print(sort_for_dict(commoditys))
