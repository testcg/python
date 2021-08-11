"""
    选择语句
        让语句有选择性的执行
        if 条件:
            满足条件执行的语句
        else:
            不满足条件执行的语句

    调试Debug
        让程序中断,逐语句审查程序执行过程与实际取值.
        1. 加断点(在可能出错的行)
        2. 开始调试(点击Debug按钮)
        3. 按F8逐语句执行,看变量取值
"""
number = int(input("请输入数字："))
# 命题：输入的是正数
# if number > 0:
#     print("正数")
# 如果
# if number < 0:
#     print("负数")
# if number == 0:
#     print("零")

if number > 0:
    print("正数")
# 否则如果
elif number < 0:
    print("负数")
# 否则
else:
    print("零")