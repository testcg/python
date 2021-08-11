"""
    函数参数
        实际参数
"""


# 位置形参：实参必填
# 缺少实参
# TypeError: func01() missing 1 required positional argument: 'p3'
# 实参过多
# TypeError: func01() takes 3 positional arguments but 4 were given
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 默认形参：实参可选
# 必须从右向左依次存在
def func02(p1=0, p2="", p3=0.0):
    print(p1)
    print(p2)
    print(p3)


# 1. 位置实参：按顺序与形参对应
func01(1, 2, 3)
# 2. 关键字实参：按名字与形参对应
# 作用:增加调用函数时的代码可读性
# 　　　指定某一个形参(跳过其他形参)
func01(p1=1, p2=2, p3=3)
func01(p2=2, p1=1, p3=3)

func02(p2="b")
func02(p1=100)
func02(100)
func02(100,p3 = 1.2)
