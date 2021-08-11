"""
    集合set
        应用2：
        数学运算
            交并补
"""
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集(相当于并且)
print(set01 & set02)  # {2, 3}

# 并集(相当于或者)
print(set01 | set02)  # {1,2,3,4}

# 补集
print(set01 - set02)  # {1}
print(set02 - set01)  # {4}
print(set01 ^ set02)  # {1, 4}
