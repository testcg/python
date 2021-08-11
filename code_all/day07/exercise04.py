"""
    练习2：二维列表
    list01 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
    ]
    1. 将第一行从左到右逐行打印
    2. 将第二行从右到左逐行打印
    3. 将第三列行从上到下逐个打印
    4. 将第四列行从下到上逐个打印
    5. 将二维列表以表格状打印

    先根据需求写死代码
    再根据规律写活代码
"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

for item in list01[0]:
    print(item)

# print(list01[1][4])
# print(list01[1][3])
# print(list01[1][2])
# print(list01[1][1])
# print(list01[1][0])
for c in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][c])

# print(list01[0][2])
# print(list01[1][2])
# print(list01[2][2])
for r in range(len(list01)):
    print(list01[r][2])

# print(list01[2][3])
# print(list01[1][3])
# print(list01[0][3])
for r in range(len(list01)-1,-1,-1):
    print(list01[r][3])

# 可读可写
for r in range(len(list01)):
    for c in range(len(list01[r])):
        print(list01[r][c],end = "\t")
    print()

# 只读
for line in list01:
    for item in line:
        print(item,end = "\t")
    print()


