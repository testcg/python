"""
    练习:
    在终端中输入任意整数，计算累加和.
    "1234" -> "1" -> 累加 1
"""
sum_value = 0
for item in input("请输入任意整数："):
    sum_value += int(item)
print(sum_value)
