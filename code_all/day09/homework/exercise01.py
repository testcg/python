# --------------------------数据--------------------------
# 商品列表
# dict_commodity_infos = {
#     1001:{"name": "屠龙刀", "price": 10000},
#     1002:{"name": "倚天剑", "price": 10000},
#     1003:{"name": "金箍棒", "price": 52100},
#     1004:{"name": "口罩", "price": 20},
#     1005:{"name": "酒精", "price": 30},
# }
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
# 3.  打印所有订单中的商品信息,
#   格式：商品名称xx,商品单价:xx,数量xx.
for order in list_orders:  # 遍历所有订单
    # order["cid"] --> 1001
    for commodity in list_commodity_infos:  # 遍历所有商品信息
        # commodity["cid"] --> 1001
        # 使用订单中的商品编号 在 商品信息中查找(商品)
        if order["cid"] == commodity["cid"]:
            print(f"商品名称{commodity['name']},商品单价:{commodity['price']},数量{order['count']}.")
            break  # 跳出内层循环

# 1.  打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
for commodity in list_commodity_infos:
    print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")

# 2.  打印商品单价小于2万的商品信息
for commodity in list_commodity_infos:
    if commodity["price"] < 20000:
        print(f"编号:{commodity['cid']}商品名称:{commodity['name']}商品单价:{commodity['price']}")

# 3. 查找单价最高的商品
max_value = list_commodity_infos[0]
for i in range(1, len(list_commodity_infos)):
    if max_value["price"] < list_commodity_infos[i]["price"]:
        max_value = list_commodity_infos[i]
print(max_value)

# 4. 根据单价升序排列
for r in range(len(list_commodity_infos) - 1):
    for c in range(r + 1, len(list_commodity_infos)):
        if list_commodity_infos[r]["price"] > list_commodity_infos[c]["price"]:
            list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
print(list_commodity_infos)
