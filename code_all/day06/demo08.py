"""
    字典dict基本操作
        删除
        遍历
"""
# 1. 删除
dict_gsx = {
    "name": "郭世鑫",
    "age": 26,
    "sex": "女"
}
del dict_gsx["sex"]
del dict_gsx["name"], dict_gsx["age"]
print(dict_gsx)

# 2. 遍历
dict_wz = {
    "name": "王志",
    "age": 22,
    "sex": "男"
}
# 获取所有key
for key in dict_wz:
    print(key)
# 获取所有value
for value in dict_wz.values():
    print(value)
# 获取所有key和value
# for item in dict_wz.items():
#     # print(item) # ('name', '王志')
#     print(item[0]) # 'name'
#     print(item[1]) # '王志'
for key,value in dict_wz.items():
    print(key)
    print(value)

# 3. 字典 --> 列表
print(list(dict_wz)) # 所有key的列表
print(list(dict_wz.values())) # 所有value的列表
# [(键1,值1),(键2,值2)]
print(list(dict_wz.items())) # 所有键值对的列表

# 练习3：
#         删除香港现有人数信息
#         删除新疆新增人数信息
#         删除上海的新增和现有信息
# 练习4：
#         在终端中打印香港字典的所有键(一行一个)
#         在终端中打印上海字典的所有值(一行一个)
#         在终端中打印新疆字典的所有键和值(一行一个)
#         在上海字典中查找值是61对应的键名称






