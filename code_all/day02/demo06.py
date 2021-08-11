"""
    核心数据类型
        str  int  float
    类型转换
        结果 = 目标类型(待转数据)
"""
# 数据类型
# 1. 字符串str:存储文字
name = "悟空"
str_number = "10" + "1"  # 字符拼接(没有数学运算)
print(str_number)  # "101"

# 2. 整形int:存储整数
int_number = 10 + 1
print(int_number)  # 11

# "10" + 1 # 在Python语言中,不支持str与int运算

# 3. 浮点型float:存储小数
float_number = 10.1

# 类型转换
# age = int(input("请输入您的年龄："))
# print("明年您" + str(age +1) + "岁了")

# 1. str --> int
result01 = int("3")  # 3
# int --> str
result02 = str(3)

# 2. str --> float
result03 = float("1.2")
#    float --> str
result04 = str(1.2)

# 3. int --> float
result05 = float(15)
#    float --> int
result06 = int(1.93)
print(result06)  # 1 向下取整

# 4. 字符串转换为其他类型时注意:
#    该字符串必须是该类型的字符表达形式(长得像)
# result07 = int("1.93")
# result08 = float("abc")
result09 = float("5")
print(result09)  # 5.0

print(12)  # 可以直接打印数值类型
print("年龄是：" + str(12))  # 因为要按照固定格式显示,所以类型转换
