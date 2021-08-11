"""
    字典推导式
"""
# 需求：根据1-10数字,生成字典的key,value是key的平方
# result = {}
# for item in range(1, 11):
#     result[item] =item ** 2
result = {item: item ** 2 for item in range(1, 11)}

# 需求：将上一个字典中key是偶数的存入另外一个字典
# new_result = {}
# for key,value in result.items():
#     if key % 2 ==0:
#         new_result[key] = value
new_result = {key: value for key, value in result.items() if key % 2 == 0}
print(new_result)
