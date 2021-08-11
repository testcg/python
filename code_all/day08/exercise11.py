"""
    练习3：根据下列代码，创建降序排列函数。
    list01 = [5, 15, 25, 35, 1, 2]
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] < list01[c]:
                list01[r], list01[c] = list01[c], list01[r]
    print(list01)
"""
def descending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                # 2. 修改可变
                list_target[r], list_target[c] = list_target[c], list_target[r]
    # 3. 不用return
    # return list_target

# 1.传入可变
list01 = [5, 15, 25, 35, 1, 2]
# new_list = descending_order(list01)
# print(new_list)
descending_order(list01)
print(list01)