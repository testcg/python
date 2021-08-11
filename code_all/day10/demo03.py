"""
    创建狗类
    数据：
        品种、昵称、身长、体重
    行为：
        吃(体重增长1)
    实例化两个对象并调用其函数
    画出内存图
"""
# 实例成员通过对象访问
# 通常在类中对象是self
#    在类外对象是 “变量=类名(...)”
class Dog:
    def __init__(self, species="", pet_name="", height=0.0, weight=0):
        self.species = species
        self.pet_name = pet_name
        self.height = height
        self.weight = weight
        self.eat()

    def eat(self):
        self.weight += 1
        print("吃饭饭~")


mx = Dog("拉布拉多", "米咻", 0.6, 60)
print(mx.weight)
mx.eat()
print(mx.weight)
