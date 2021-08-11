"""
    重写内置函数 - 算数运算符
        改变其行为
"""


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x的分量是:{self.x},y分量{self.y}"

    # 自定义对象可以使用 +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
print(pos03)
