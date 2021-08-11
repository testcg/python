"""
    算法
        1. 变量交换 a,b = b,a
        2. 计算最值
        3. 累计运算
        4. 排序(升序排列)
"""
list01 = [42, 15, 56]
"""
# 将最小元素存储到第一个位置
for c in range(1, len(list01)):
    if list01[0] > list01[c]:
        list01[0], list01[c] = list01[c], list01[0]
print(list01)
# 将最小元素存储到第二个位置
for c in range(2, len(list01)):
    if list01[1] > list01[c]:
        list01[1], list01[c] = list01[c], list01[1]
print(list01)
# 将最小元素存储到第..个位置
"""
# 取数据(不要最后一个)
for r in range(len(list01) - 1):  # 0    1
    # 作比较(从下一个开始)
    for c in range(r + 1, len(list01)):
        # 找更小
        if list01[r] > list01[c]:
            # 则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
