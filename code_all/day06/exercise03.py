"""
    练习：
    生成10--30之间能被3或者5整除的数字
    [10, 12, 15, 18, 20, 21, 24, 25, 27]
    生成5 -- 20之间的数字平方
    [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
"""
# result = []
# for item in range(10,31):
#     if item % 3 ==0 or item % 5 ==0:
#         result.append(item)

result = [item for item in range(10,31)if item % 3 ==0 or item % 5 ==0]
print(result)

result = [item ** 2 for item in range(5,21)]
print(result)


