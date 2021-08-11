"""
    练习1：对象计数器
    统计构造函数执行的次数
            使用类变量实现
            画出内存图
    class Wife:
        pass

    w01 = Wife("双儿")
    w02 = Wife("阿珂")
    w03 = Wife("苏荃")
    w04 = Wife("丽丽")
    w05 = Wife("芳芳")
    Wife.print_count()# 总共娶了5个老婆
"""


class Wife:
    # 用类变量表达多个对象的相同数据
    count = 0

    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.count}个老婆")

    def __init__(self, name=""):
        # 用实例变量表达多个对象的不同数据
        self.name = name
        Wife.count += 1


w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
Wife.print_count()  # 总共娶了5个老婆
