"""
    跨类调用
        请以面向对象的思想,描述下列情景.
            老张开车去东北
            老李开车去东北
            老王开车去东北
        创建人类,车类,而不创建东北类(没有行为,没有过多数据).
"""
# 用类区分行为不同
# 用对象区分数据不同

# 1. 直接创建对象
#    语义：老张每次去东北都开一辆新车
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position):
        print(self.name,"去",position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("汽车行驶")
 
lz = Person("老张")
ll = Person("老李")
lw = Person("老王")

lz.go_to("东北")
"""

# 2. 在构造函数创建对象
#    语义：老张每次去东北都开自己的车
"""
class Person:

    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self,position):
        print(self.name,"去",position)
        self.car.run()

class Car:
    def run(self):
        print("汽车行驶")

lz = Person("老张")
lz.go_to("东北")
"""

# 3. 在使用时创建对象(通过参数传入)
#    语义：老张每次去东北用交通工具
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self,position,vehicle):
        print(self.name,"去",position)
        vehicle.run()

class Car:
    def run(self):
        print("汽车行驶")

lz = Person("老张")
car = Car()
lz.go_to("东北",car)