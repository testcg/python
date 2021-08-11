"""
    重写自定义函数 - 面向对象精髓
"""
# 老张开车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print(self.name, "去", position)
        vehicle.run()


class Car:
    def run(self):
        print("嘟嘟嘟~")


lz = Person()
c = Car()
lz.go_to("东北", c)
"""


# 要求：日后可能坐飞机,划船,骑车...
# 缺点：违背开闭原则(增加新功能,不修改客户端代码)

class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print(self.name, "去", position)
        # 根据不同类型,决定不同行为(行驶/飞行)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("嘟嘟嘟~")

class Airplane:
    def fly(self):
        print("嗖嗖嗖~")

lz = Person()
c = Car()
a = Airplane()
lz.go_to("东北", c)
lz.go_to("东北", a)
