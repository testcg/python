"""
    改造
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print(self.name, "去", position)
        if isinstance(vehicle, Vehicle):
            # 先行确定用法
            # 编码时调用交通工具(爸爸)
            # 运行时执行汽车(儿子)
            vehicle.transport()
            

# 练习1：以面向对象思想，描述下列情景：
#     情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
#     变化：还可能伤害房子、树、鸭子....
#     要求：增加新事物，不影响手雷.
#     画出架构设计图

class Vehicle:
    def transport(self):
        pass


class Car(Vehicle):

    def transport(self):
        print("嘟嘟嘟~")


class Airplane(Vehicle):
    def transport(self):
        print("嗖嗖嗖~")


lz = Person()
c = Car()
a = Airplane()
lz.go_to("东北", c)
lz.go_to("东北", a)
lz.go_to("东北", "汽车")
