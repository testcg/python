"""
    列表推导式
        列表 = [对变量操作 for 变量 in 可迭代对象]
        列表 = [对变量操作 for 变量 in 可迭代对象 if 条件]
"""
list01 = [432, 5, 54, 6, 76, 87]
# 需求：将大于10的元素存储新列表
# list02 = []
# for item in list01:
#     if item > 10:
#         list02.append(item)
list02 = [item for item in list01 if item > 10]
print(list02)
# 需求：将元素的个位存储在新列表
# list03 = []
# for item in list01:
#         list03.append(item % 10)
list03 = [item % 10 for item in list01]
