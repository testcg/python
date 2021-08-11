"""
    函数 - 参数
        使用功能时 给 定义功能时 传递的信息
    设计理念：崇尚小而精,拒绝大而全
"""


# 定义攻击功能
def attack(count):  # 形式参数：表面的,抽象的,没有具体数据
    for __ in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")
        print("肘击")
        print("鞭腿")

# 使用攻击功能
attack(3)  # 实际参数：具体的,真实的,有数据
# count = 10
# attack(count)
number = 10
attack(number)  # 传递的是数据,与变量名无关.
