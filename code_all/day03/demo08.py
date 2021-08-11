"""
    条件表达式
        变量 = 满足条件的值 if 条件 else 不满足条件的值
"""
# 根据一个条件,为变量赋值
# if input("请输入性别:") == "男":
#     value = 1
# else:
#     value = 0

value = 1 if input("请输入性别:") == "男" else 0
print(value)
