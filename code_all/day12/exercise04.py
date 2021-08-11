"""

"""


class Color:
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

c01 = Color(0, 100, 200, 255)
c02 = Color(100, 0, 0, 255)
c03 = c01 * c02
print(c03)
