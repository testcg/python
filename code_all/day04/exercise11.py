"""
    练习：
    在终端中获取一个整数，作为边长，打印矩形
"""
number = int(input("请输入整数："))
print("*" * number)

for __ in range(number - 2):
    print("*%s*" % (" " * (number - 2)))

print("*" * number)
