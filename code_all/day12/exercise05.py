"""
    练习:在Color类中实现下列效果
"""


class Color(object):
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __mul__(self, other):
        r = self.r * other.r
        g = self.g * other.g
        b = self.b * other.b
        a = self.a * other.a
        return Color(r, g, b, a)

    def __imul__(self, other):
        if type(other) == Color:
            self.r *= other.r
            self.g *= other.g
            self.b *= other.b
            self.a *= other.a
        else:
            self.r *= other
            self.g *= other
            self.b *= other
            self.a *= other
        return self


c01 = Color(0, 100, 200, 255)
c02 = Color(100, 0, 0, 255)
c01 *= c02
c01 *= 2
print(c01)
