"""
    练习:创建颜色列表,测试in、count、index、remove
                  sort、max、min
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.a > other.a


list_colors = [
    Color(150, 0, 0, 255),
    Color(200, 0, 0, 255),
    Color(200, 0, 0, 255),
    Color(0, 200, 0, 255),
    Color(0, 0, 200, 255),
    Color(0, 0, 0, 255),
]
print(list_colors.count(Color(200, 0, 0, 255)))

print(max(list_colors))
# 升序排列
list_colors.sort()
# 降序排列
list_colors.sort(reverse=True)
print(list_colors)
