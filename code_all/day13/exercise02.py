"""
    练习2：创建图形管理器
        1. 记录多种图形（圆形、矩形....）
        2. 提供计算总面积的方法.
        满足：
            开闭原则
        测试：
            创建图形管理器，存储多个图形对象。
            通过图形管理器，调用计算总面积方法.
    封装(分)：创建了GraphicsManager、Circle、Rectangle
    继承(隔)：创建了Graphics,隔离GraphicsManager和Circle、Rectangle的变化
    多态(做)：Circle重写了Graphics的get_area方法
             Rectangle重写了Graphics的get_area方法
"""

"""
class GraphicsManager:
    def __init__(self):
        self.all_graphics = []

    def calculate_total_area(self):
        total_area = 0
        for item in self.all_graphics:
            # 多态
            # 编码时调用图形
            # 运行时执行矩形、圆形
            total_area += item.get_area()
        return total_area

class Graphics:
    def get_area(self):
        pass

class Circle(Graphics):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2

class Rectangle(Graphics):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w

manager = GraphicsManager()
manager.all_graphics.append(Circle(5))
manager.all_graphics.append(Rectangle(2, 3))
print(manager.calculate_total_area())
"""


class GraphicsManager:
    def __init__(self):
        self.__all_graphics = []

    @property
    def all_graphics(self):
        return self.__all_graphics

    def add_graphics(self, graph):
        if isinstance(graph, Graphics):
            self.__all_graphics.append(graph)

    def calculate_total_area(self):
        total_area = 0
        for item in self.__all_graphics:
            total_area += item.get_area()
        return total_area


class Graphics:
    def __init__(self, name=""):
        self.name = name

    def get_area(self):
        pass


class Circle(Graphics):
    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2


class Rectangle(Graphics):
    def __init__(self, name, l, w):
        super().__init__(name)
        self.l = l
        self.w = w

    def get_area(self):
        return self.l * self.w


manager = GraphicsManager()
manager.add_graphics(Circle("圆形", 5))
manager.add_graphics(Rectangle("矩形", 2, 3))
manager.add_graphics("三角")
# 打印所有图形总面积
print(manager.calculate_total_area())
# 打印所有图形名称
for item in manager.all_graphics:
    print(item.name)
