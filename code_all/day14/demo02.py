"""
    多继承 - 复用代码不灵活
"""
class A:
    def func01(self):
        print("func01")

class B:
    def func02(self):
        print("func02")

# 优点：最简单的代码复用方式(C在使用AB)
# 缺点：增加新类型,必须修改C类.违反开闭原则
class C(A,B):
    def func03(self):
        self.func01()
        self.func02()
