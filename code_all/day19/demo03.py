"""
    闭包应用
        逻辑连续
            从得一次钱,可以花多次钱
"""


def give_gife_money(money):  # 得钱
    print("获得", money, "元压岁钱")
    def child_buy(commodity, price): # 花钱
        nonlocal money
        money -= price
        print("购买了", commodity, "花了", price, "元,还剩下", money)
    return child_buy

# 调用外部函数
action = give_gife_money(500)
# 调用内部函数
action("变形金刚", 200)
action("芭比娃娃", 300)
# 练习：使用闭包模拟以下情景：
#     在银行开户存入10000
#     购买xx商品花了xx元
#     购买xx商品花了xx元
