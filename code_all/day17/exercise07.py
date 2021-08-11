# day12/exercise07.py
class Commodity:
    def __init__(self, cid, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]


# 要求：使用生成器函数和生成器表达式完成
# 练习1:查找商品编号小于1003的所有商品
def find_commoditys_by_cid():
    for cmd in list_commodity_infos:
        if cmd.cid < 1003:
            yield cmd


for item in find_commoditys_by_cid():
    print(item.__dict__)

commoditys_by_cid = (cmd for cmd in list_commodity_infos if cmd.cid < 1003)
for item in commoditys_by_cid:
    print(item.__dict__)


# 练习2:查找商品名称大于2个字的所有商品
def find_commoditys_by_name():
    for cmd in list_commodity_infos:
        if len(cmd.name) > 2:
            yield cmd


for item in find_commoditys_by_name():
    print(item.__dict__)

commoditys_by_name = (cmd for cmd in list_commodity_infos if len(cmd.name) > 2)
for item in commoditys_by_name:
    print(item.__dict__)


# 练习3:查找商品单价大于10000元的所有商品名称
def get_commodity_names():
    for cmd in list_commodity_infos:
        if cmd.price > 10000:
            yield cmd.name


for item in get_commodity_names():
    print(item)

commodity_names = (cmd.name for cmd in list_commodity_infos if cmd.price > 10000)
for item in commodity_names:
    print(item)


# 练习4:查找单价最便宜的商品信息(自定义函数)
def get_min_by_price():
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if min_value.price > list_commodity_infos[i].price:
            min_value = list_commodity_infos[i]
    return min_value


min_value = get_min_by_price()
print(min_value.__dict__)
