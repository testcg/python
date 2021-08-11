"""
    函数返回值语法
"""
def func01():
    print("func01执行了")
    return 100

# 调用函数接收返回值
re = func01()
print(re)
# 调用函数不接收返回值
func01()

# return 后面没有数据,相当于返回None
def func02():
    print("func02执行了")
    return

re = func02()
print(re)

# return可以退出函数
def func03():
    print("func03执行了")
    return
    print("func03又执行了")

func03()

def func04():
    # 一个break只能退出一层循环
    # while True:
    #     while True:
    #         break
    #     break
    while True:
        while True:
            return # 退出函数(多少层循环都结束)

def func05():
    print("func05执行了")

re = func05()
print(re) # None