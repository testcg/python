"""
    总复习 - Python 核心
    一、自动化内存管理机制
        1. 引用计数：
            每个对象记录被变量绑定(引用)的数量,
            当为0时被销毁。
            缺点-循环引用：
                两个垃圾互相引用,但是计数不为0

        2. 标记清除
            全盘扫描,标记不再使用的数据
           缺点-速度慢

        3. 分代回收
            程序运行时,将内存分为小0、中1、大2三块.
            每次创建新数据,一定在0代分配空间.
            如果内存告急,触发标记清除
            再将有用的数据升代,清空上一代

        内存优化：尽少产生垃圾、对象池、配置垃圾回收器参数

    二、跳转语句

    三、函数参数
        实际参数：与形参进行对应
            位置实参:按顺序
                函数名(数据1,数据2)
            序列实参：拆
                函数名(*序列)
            关键字实参:按名字
                函数名(形参名1 = 数据1,形参名2 = 数据2)
            字典实参：拆
                函数名(**字典)

        形式参数
            位置形参:必填
                def 函数名(形参名1,形参名2)
            默认形参:可选
               def 函数名(形参名1=默认值,形参名2=默认值)
            星号元组形参：收集位置实参
                 def 函数名(*args)
            双星号字典形参：收集关键字实参
                 def 函数名(**kwargs)
            命名关键字形参：必须是关键字实参
                 def 函数名(*args,形参名)
                 def 函数名(形参名,*,形参名)
"""
def func01(p1,p2):
    pass

func01(p1 =1 ,p2 =2)


list01 = []  # 引用计数+=1
list02 = list01  # 引用计数+=1
del list01  # 引用计数-=1
list02 = []  # 引用计数-=1

list01 = []
list02 = []
list01.append(list02)
list02.append(list01)
del list01, list02  # 循环引用

# 循环拼接字符串会不断产生垃圾
# str_result = ""
# for i in range(10):
#     str_result += str(i)
# print(str_result)

# 向列表添加元素,不会产生垃圾
result = []
for i in range(10):
    result.append(str(i))
print("".join(result))

# 对象池
# 每次创建数据时,都先判断池中是否存在相同数据
# 如果存在直接返回地址,如果不存在则创建新数据
data01 = ["10.1234",]
data02 = ["10.1234",]
print(id(data01))
print(id(data02))

# 跳转语句
def func01():
    while True:
        while True:
            break # 1.跳出
            continue # 2.跳过
            return "单个数据" # 3. 退出

def func02():
    yield "多个数据" # 4. 暂时离开

def func03():
    raise Exception("错误信息") # 5. 不断上翻