"""
    定义函数,根据商品编号,删除商品信息,返回是否删除成功
    list_commodity_infos.remove( 商品编号  )
"""


class Commodity:
    def __init__(self, cid, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.cid == other


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]


def delete_commodity(cid):
    """
        根据商品编号,删除商品信息,返回是否删除成功
    :param cid: 需要删除的商品编号
    :return: 是否删除成功
    """
    if cid in list_commodity_infos:
        list_commodity_infos.remove(cid)
        return True
    return False


print(delete_commodity(1009))  # True
print(list_commodity_infos)
