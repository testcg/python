"""
    Enclosing  外部嵌套作用域
        内部函数可以读取外部函数变量
        如果修改必须使用nonlocal声明
"""


def func01():
    # 局部变量
    # 外部嵌套变量
    a = 10
    print("func01,",a)

    def func02():  # 内部函数
        print("func02,",a)

    func02() # 只能在函数内部方法


func01()
# 无法在函数外访问内部函数
# func02()


def func03():
    a = 10
    def func04():
        # a = 20 # 创建了func04的局部变量

        nonlocal a
        a = 20
        print("func04,",a) # 20

    func04()
    print("func03,", a) # 10


func03()