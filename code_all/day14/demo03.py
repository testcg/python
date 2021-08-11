"""
    多继承 - 复用代码不灵活
"""
"""
class A:
    def func01(self):
        print("A -- func01")

class B:
    def func01(self):
        print("B -- func01")

class C(A,B):
    def func01(self):
        print("C -- func01")
        super().func01() # A
        # 此时必须通过类名调用,否则不能执行后面的同名方法
        B.func01(self) # B

c = C()
c.func01()
"""

class A:
    def func01(self):
        print("A -- func01")

class B(A):
    def func01(self):
        print("B -- func01")
        super().func01()

class C(A):
    def func01(self):
        print("C -- func01")
        super().func01()

class D(B,C):
    def func01(self):
        print("D -- func01")
        super().func01()

d = D()
d.func01() # D -> B -> C -> A
print(D.mro())