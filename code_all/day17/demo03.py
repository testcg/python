"""
    zip
"""
list_name = ["郭世鑫", "万忠刚", "赵文杰"]
list_age = [22, 26]

# for 变量 in zip(可迭代对象1,可迭代对象2)
for item in zip(list_name, list_age):
    print(item)

# 应用:矩阵转置
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4]
]
# new_map = []
# for item in zip(map[0],map[1],map[2],map[3]):
#     new_map.append(list(item))
# print(new_map)

# new_map = []
# for item in zip(*map):
#     new_map.append(list(item))

new_map = [list(item) for item in zip(*map)]
print(new_map)
