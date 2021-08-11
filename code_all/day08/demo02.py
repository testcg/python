"""
    函数 - 入门
        价值：减少代码的重复
        语法：
            def 函数名(?):
                函数体

            函数名()
"""
# 代码的重复是万恶之源
"""
# 做法(变化) + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ...
# 做法(变化) + 用法
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""


# 定义函数-做法(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")
    print("鞭腿")

# 用法
attack()
# ...
# 用法
attack()
