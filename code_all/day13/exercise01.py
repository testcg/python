"""
    练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图

    面向对象三大特征：
        封装(分)：创建了手雷、敌人、玩家
        继承(隔)：创建了目标类,隔离手雷与敌人、玩家的变化
        多态(做)：敌人对于受伤做的是头顶爆字
                 玩家对于受伤做的是碎屏
"""

"""
版本1：一次炸一个

class Grenade:
    def explode(self, target):
        print("爆炸啦")
        # 编码时调用父类
        # 运行时执行子类
        target.damage()  # 不管是不是鸭子,只要有鸭子叫都行


class Target:  # 鸭子
    def damage(self):
        pass


class Player(Target):
    def damage(self):
        print("碎屏")


# "小鸭子原则":狗、猫只要是会像鸭子一样叫,就认为是鸭子
class Enemy:  # 狗
    def damage(self):  # 鸭子叫
        print("头顶爆字")


g = Grenade()
p = Player()
g.explode(p)
g.explode(Enemy())
"""


# 版本2：一次炸多个
class Grenade:
    def explode(self, *args):  # 多实参合一元组
        print("爆炸啦")
        for target in args:
            target.damage()


class Target:  # 鸭子
    def damage(self):
        pass


class Player(Target):
    def damage(self):
        print("碎屏")


# "小鸭子原则":狗、猫只要是会像鸭子一样叫,就认为是鸭子
class Enemy:  # 狗
    def damage(self):  # 鸭子叫
        print("头顶爆字")


g = Grenade()
g.explode(Player(), Enemy())
