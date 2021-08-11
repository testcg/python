"""
    练习1:请排列出2个色子可以组成的所有可能(列表)
    色子(1~6)    range(1,7)
    色子(1~6)
    练习2:请排列出3个色子可以组成的所有可能(列表)
"""
# result = []
# for x in range(1, 7):
#     for y in range(1, 7):
#         result.append((x , y))
result = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(result)

# result = []
# for x in range(1, 7):  # 1          2
#     for y in range(1, 7):  # 1           2      ...
#         for z in range(1, 7):  # 123456  123456   ...
#             result.append((x, y, z))

result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(result)
