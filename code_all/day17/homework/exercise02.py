"""
    迭代器 --> yield
"""


class CommodityController:
    def __init__(self):
        self.__commoditys = []

    def add_commodity(self, cmd):
        self.__commoditys.append(cmd)

    def __iter__(self):
        index  = 0
        yield self.__commoditys[index]

        index += 1
        yield self.__commoditys[index]

        index += 1
        yield self.__commoditys[index]

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)

# iterator = controller.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break
