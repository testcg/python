"""
练习：写出下列代码在终端中执行效果
"""
class A:
    def func01(self):
        print("A")
        super().func01()


class B:
    def func01(self):
        print("B")


class C(A,B):
    def func01(self):
        print("C")
        super().func01()


class D(A, B):
    def func01(self):
        print("D")
        super().func01()


class E(C,D):
    def func01(self):
        print("E")
        super().func01()

e = E()
e.func01() # E -> C -> D -> A -> B