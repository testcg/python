"""
    函数式编程
        将函数赋值给变量
"""


def func01():
    print("func01执行了")


def func02():
    print("func02执行了")


def func04(p1, p2):
    print("func04,参数是：", p1, p2)


def func03(func):
    print("func03执行了")
    # func02() # 固定了func03与func02的调用关系
    # 只能调用无参数无返回值函数
    func()  # 由使用者决定调用哪个函数[灵活]


# 直接调用函数
func01()
# 将函数赋值给变量(右边的函数一定不能写小括号)
a = func01
# 间接调用函数
a()

func03(func02)
func03(func01)
# 报错,由于func03【先确定】的调用方法(无参数),
# 所以【后定义】的func04因为有参数所以不能传递进来
# func03(func04)
