"""
    练习3：以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""
class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        # 对于敌人受伤的功能,玩家应该是使用关系
        # 而不是制作关系
        print("攻击")
        target.damage(self.atk)

class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self,value):
        print("头顶爆字")
        self.hp -= value

player = Player(25)
enemy1 = Enemy(50)
enemy2 = Enemy(80)
player.attack(enemy1)
player.attack(enemy2)
print(enemy1.hp)
print(enemy2.hp)