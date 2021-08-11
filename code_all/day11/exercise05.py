"""
    练习4：以面向对象思想,描述下列情景.
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经
    张无忌工作挣了5000元
    赵敏工作挣了10000元
    经过分析发现：张无忌与赵敏属于数据不同
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)

    def work(self,money):
        print(self.name,"上班涨了",money)

zwj = Person("张无忌")
zm = Person("赵敏")

zwj.teach(zm,"九阳神功")
zm.teach(zwj,"玉女心经")

zwj.work(5000)
zm.work(10000)
