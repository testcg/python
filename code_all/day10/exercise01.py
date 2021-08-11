"""
    练习：创建手机类
      数据：品牌、价格、颜色
      行为：通话
      实例化两个对象并调用其函数
      画出内存图
"""


# 所有单词首字母大写,多个单词之间不要用下划线隔开
class MobilePhone:
    def __init__(self, brand, price, color="白色"):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + "在通话")


huawei = MobilePhone("华为P40", 6000, "黑色")
iphone = MobilePhone("苹果12", 10000)

huawei.call()
iphone.call()
