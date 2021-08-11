"""
    重写内置函数 - 比较运算符
        定义自定义对象比较相同的依据
                       大小

"""

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x的分量是:{self.x},y分量{self.y}"

    # 相同依据
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # 大小依据
    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2
        # return self.x < other.x


pos01 = Vector2(1, 2)
pos02 = Vector2(1, 2)
print(pos01 == pos02)  # (默认)按地址 False  按内容True
print(pos01 is pos02)  # 按地址 False
# print(id(pos01) == id(pos02))

list_position = [
    Vector2(2, 2),
    Vector2(5, 5),
    Vector2(3, 3),
    Vector2(1, 1),
    Vector2(4, 4),
]
# 重写 __eq__
print(Vector2(5, 5) in list_position)
print(list_position.count(Vector2(1, 1)))
list01 = [10]
list02 = [10]
print(list01 == list02)  # True 按内容
print(list01 is list02)  # False 按地址

# 重写 __lt__
list_position.sort()
print(list_position)  # 加断点调试查看列表元素
