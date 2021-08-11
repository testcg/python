"""
    练习2：以面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(头顶爆字).
"""


class Player:
    def attack(self, target):
        print("攻击")
        target.damage()


class Enemy:
    def damage(self):
        print("头顶爆字")


player = Player()
enemy = Enemy()
player.attack(enemy)
