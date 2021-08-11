"""
    函数内存分配
"""

# 1. 将函数代码加载到内存中的代码区
def func01(p1):
    print("func01执行了,参数是:" + p1)
    return 100

data01 = "悟空"
# 2. 调用函数时,会开辟一块空间(栈帧),存储在函数中定义的变量.
re = func01(data01)
# 3. 函数执行后,立即释放该空间
print(re) # 100


def func02(p1,p2):
     p1 = "猪八戒"
     p2[0] = 500

data02 = "八戒"
data03 = [50]
func02(data02,data03)
print(data02) # ?
print(data03) # ?


