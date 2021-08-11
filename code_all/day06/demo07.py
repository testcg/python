"""
    字典dict基本操作
        添加
        定位
"""
dict_gsx = {
    "name": "郭世鑫",
    "age": 26,
    "sex": "女"
}
# 添加
if "money" not in dict_gsx:
    dict_gsx["money"] = 1000000

# 定位 - key
# -- 修改
if "age" in dict_gsx:
    dict_gsx["age"] = 27
# -- 读取
print(dict_gsx["name"])
#     练习2：
#         在终端中打印香港的现有人数
#         在终端中打印上海的新增和现有人数
#         新疆新增人数增加1
