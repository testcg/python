"""
    算数运算符
        +  -  *  /  //  %  **
    增强运算符:在算数运算符基础上增加了对自身赋值的功能
        +=  -=  *=  /=  //=  %=  **=
"""
# 1. 算数运算符
number01 = 5
number02 = 2
# 幂运算 5 的 2次方
print(number01 ** number02)  # 25
print(number01 // number02)  # 2
print(number01 / number02)  # 2.5
print(number01 % number02)  # 1

# 2. 增强运算符
number03 = 10
number03 + 5
print(number03)  # 10

number04 = 10
# number04 = number04 + 5
number04 += 5
print(number04)  # 15
