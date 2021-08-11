"""
    父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    使用属性保护速度在0~260,电池容量在0~10000范围内
    直接打印对象格式：
        xx的速度是xx
        xx的速度是xx,电池容量是xx,充电功率是xx
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 260:
            self.__speed = value
        else:
            raise Exception("速度异常")

    def __str__(self):
        return f"{self.brand}的速度是{self.speed}"


class ElectricCars(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value):
        if 0 <= value <= 10000:
            self.__battery_capacity = value
        else:
            raise Exception("容量异常")

    def __str__(self):
        super().__str__()
        # return f"{self.brand}的速度是{self.brand},电池容量是{self.battery_capacity},充电功率是{self.charging_power}"
        return super().__str__() + f",电池容量是{self.battery_capacity},充电功率是{self.charging_power}"


bc = Car("奔驰", 220)
print(bc)

am = ElectricCars("艾玛", 180, 10000, 220)
print(am)
