"""
    现实世界               虚拟世界
    客观事物  -抽象化->  类     -实例化->   对象
     奔驰汽车          汽车类            汽车对象
     宝马汽车          品牌               奔驰
                     车牌号             京C...
                     颜色               白色
                     ....               ...
"""


class Wife:
    """
        抽象的老婆类(概念)
    """

    # 数据（通过构造函数创建）
    def __init__(self, name, height=160, weight=100):
        # print(id(self))
        # 实例变量
        self.name = name
        self.height = height
        self.weight = weight

    # 行为
    def play(self):
        print(self.name + "在玩耍")


tc = Wife("铁锤", 190, 200)
# print(id(tc))
print(tc.name)
tc.play()

ch = Wife("翠花", 160, 100)
print(ch.name)
ch.play()
