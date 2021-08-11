"""
练习1：将昨天作业day09/homework/exercise01功能改为函数
练习2：在终端中根据输入的选项,调用相应功能
"""
# ---------------全局变量-----------------------
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]


# ---------------定义函数-----------------------

def print_single_commodity(commodity):
    print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")


# 1. 打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_all_commodity():
    for commodity in list_commodity_infos:
        # print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")
        print_single_commodity(commodity)


# 2. 打印商品单价小于2万的商品信息
def print_commodity_price_lt_2w():
    for commodity in list_commodity_infos:
        if commodity["price"] < 20000:
            # print(f"编号:{commodity['cid']}商品名称:{commodity['name']}商品单价:{commodity['price']}")
            print_single_commodity(commodity)


# 3. 查找单价最高的商品
def find_commodity_max_price():
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value["price"] < list_commodity_infos[i]["price"]:
            max_value = list_commodity_infos[i]
    return max_value


# 4. 根据单价升序排列
def sort_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r]["price"] > list_commodity_infos[c]["price"]:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


def display_menu():
    """
        显示菜单
    """
    print("输入1键显示所有商品信息")
    print("输入2键显示单价大于2w的商品")
    print("输入3键显示最贵的商品")
    print("输入4键按照单价显示所有商品")


def select_menu():
    """
        选择菜单
    """
    item = input("请输入您的选项：")
    if item == "1":
        print_all_commodity()
    elif item == "2":
        print_commodity_price_lt_2w()
    elif item == "3":
        cmd = find_commodity_max_price()
        print_single_commodity(cmd)
    elif item == "4":
        sort_by_price()
        print_all_commodity()


def main():
    while True:
        display_menu()
        select_menu()


# ---------------入口代码-----------------------
main()

"""
data01 = 10 
def func01(): 
    data01 = 20 # 希望修改全局变量,但是创建了局部变量

data02 = [10] 
def func02():
    # 读取全局变量,修改列表第一个元素
    data02[0] = 20
"""
