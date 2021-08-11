"""
    lambda 表达式
        定义：
            匿名方法
        语法：
            lambda 参数:函数体
        注意：
            lambda能表达的函数,def都能表达
            但是lambda不支持赋值语句,不支持多条语句
"""

# def func01(p1,p2):
#     return p1 > p2
#
# print(func01(1,2)) #  False

# 写法1:有参数有返回值
func01 = lambda p1, p2: p1 > p2
print(func01(1, 2))

# def func02():
#     return 100
#
# print(func02())  #

# 写法2:无参数有返回值
func02 = lambda: 100
print(func02())

# def func03(p1):
#     print("参数是：",p1)
#
# func03(200)

# 写法3:有参数无返回值
func03 = lambda p1: print("参数是：", p1)
func03(200)

# def func04():
#     print("func04执行了")
#
# func04()

# 写法4:无参数无返回值
func04 = lambda: print("func04执行了")
func04()


# 注意1: lambda 不支持赋值语句
def func05(p1):
    p1[0] = 1000


list01 = [10]
func05(list01)
print(list01)  # 1000


# func05 = lambda p1:p1[0] = 1000

# 注意2:lambda 不支持多条语句
def func06():
    for i in range(5):
        print(i)


func06()

# func06 = lambda :for i in range(5):print(i)
