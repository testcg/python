"""
    练习4：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力,减少血量,头顶爆字).
        --敌人还能攻击玩家,玩家受伤
                (根据敌人攻击力,减少血量,闪现红屏).
        --敌人玩家血量没有时,都会死亡(播放死亡动画)　
"""


# 现状：
# 两个类存在 完全相同的代码
#          部分相同的代码

class Player:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("闪现红屏")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("播放死亡动画")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        print("头顶爆字")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("播放死亡动画")

    def attack(self, target):
        print("攻击")
        target.damage(self.atk)


player = Player(100, 50)
enemy = Enemy(80, 25)

player.attack(enemy)
enemy.attack(player)
player.attack(enemy)
