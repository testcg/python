"""
# 练习1：将列表中所有奇数设置为None
# 练习2：将列表中所有偶数自增1
"""
list01 = [31, 34, 54, 56, 677, 8]
# for i, item in enumerate(list01):
#     if item % 2:
#         list01[i] = None

# itere + 回车
for i, item in enumerate(list01):
    if item % 2 == 0:
        list01[i] += 1
print(list01)
