"""
    列表转换为字符串：
	result = "连接符".join(列表)
"""
list01 = ["a", "b", "c"]
result = "_".join(list01)
print(result)  # a_b_c

# 应用
# 需求:根据某个逻辑循环拼接字符串
#       0-9
# result = ""
# for number in range(10):
#     # 缺点：每次循环都会产生新字符串,产生垃圾
#     result += str(number)
# print(result)  # 0123456789

# 解决：将不可变数据改为可变数据
result = []
for number in range(10):
    result.append(str(number))
result = "".join(result)
print(result)  # 0123456789
