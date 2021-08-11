"""
    逻辑运算符:判断两个命题之间关系的运算符
        与或非
"""
# 短路逻辑：
# 一但结果确定，后面的语句将不再执行。
# 作用：尽量将复杂(耗时)的判断放在后面

# 1. 与
# 有钱  并且  有房
# 两个条件都得满足
# 如果前面条件不满足,后面条件不判断,结论不成立False
# 现象：一假俱假
# print(int(input("请输入存款:")) >= 1000000 and int(input("请输入几套房:")) >= 1)

# print(True and True)  # True
# print(False and True)  # False
# print(True and False)  # False
# print(False and False)  # False

# 2. 或
# 有钱  或者  有房
# 两个条件满足一个就行
# 如果前面条件满足,后面条件不判断,结论成立True
# 现象：一真俱真
# print(int(input("请输入存款:")) >= 1000000 or int(input("请输入几套房:")) >= 1)
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# 3. 非：取反
print(not True)  # False
