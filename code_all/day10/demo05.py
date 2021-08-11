"""
    类成员
        类变量
        类方法
"""
# 类变量：    总行的钱、饮水机、加油站油...
# 实例变量：  支行的钱、杯子、汽车油...

class ICBC:
    """
        工商银行
    """
    # 类变量：总行的钱   [大家]
    total_money = 1000000

    @classmethod
    def print_total_money(cls):
        # print("总行的钱:%d" % ICBC.total_money)
        print("总行的钱:%d" % cls.total_money)

    def __init__(self, name="", money=0):
        self.name = name
        # 实例变量：支行的钱   [各自]
        self.money = money
        # 创建支行时,总行的钱减少
        ICBC.total_money -= money


tt = ICBC("天坛支行", 100000)
xd = ICBC("西单支行", 200000)
print(ICBC.total_money)
ICBC.print_total_money()
