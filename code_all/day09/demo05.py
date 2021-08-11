"""
    函数参数
        形式参数
            命名关键字形参
"""


# 要求：实参必须是关键字实参
# 作用：传递信息更明确
def func01(*args, p1):
    print(args)
    print(p1)


def func02(p1, *, p2):
    print(p1)
    print(p2)


func02(1, p2=2)

# 应用
# def print(*args, sep=' ', end='\n')
print(1, 2, 3, sep="_")
print("*", end=" ")
print("*", end=" ")

print("a", "b", "c", sep='/', end=" ")
# print("a","b","c",'/'," ")
