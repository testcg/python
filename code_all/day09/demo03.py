"""
    函数参数
        形式参数
            星号元组形参
            双星号字典形参
"""


# 实参数量无限
# -- 只支持位置实参
def func01(*p1):  # 多　合　一(元组)
    print(p1)


# -- 只支持关键字实参
def func02(**p1):  # 多　合　一(字典)
    print(p1)


def func03(*args, **kwargs):
    print(args)
    print(kwargs)


func01()
func01(1, 2)  # (1, 2)

func02()
func02(p1=1, p2=2)  # {'p1': 1, 'p2': 2}

func03()
func03(1, 2, 3)
func03(p1=1, p2=2)
# (1, 2, 3){'p1': 1, 'p2': 2}
func03(1, 2, 3, p1=1, p2=2)

# 实参顺序：先位置再关键字
# func03(1, 2, p1=1, 3, p2=2)
# func03(p1=1, p2=2, 1, 2, 3)
