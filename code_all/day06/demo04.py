"""
    面试题：Python有哪些数据类型?
        可变类型:预留空间 + 自动扩容
            例如：list
            优点：使用方便
        不可变类型:按需分配
            例如：tuple str  int  float  bool ...
            优点：节省内存

    元组tuple基础操作
        创建
        定位(读取)
        遍历
"""
# 1. 创建
# 语法1:元组名 = (元素1,元素2)
tuple01 = (10, 20, 30)
# 语法2:元组名 = tuple(可迭代对象)
# 在计算过程中,使用列表存储数据
list01 = ["数据1", "数据2", "数据3"]
# 计算完成后,使用元组存储结果
tuple02 = tuple(list01)

# 2. 定位
# --索引
print(tuple01[1])
# --切片(创建新元组)
print(tuple01[-2:])

# 3. 遍历
# 快捷键:
# iter + 回车
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 4. 创建元组时,在没有歧义的情况下,可以省略括号
tuple03 = "a", "b", "c"

# 5. 拆包
data01, data02, data03 = tuple03
data01, data02, data03 = [1, 2, 3]
data01, data02, data03 = "孙悟空"
print(data01)
print(data02)
print(data03)
# * 表示接收剩余的元素
*data01, data02 = [1, 2, 3]
data01, *data02, data03 = (1, 2, 3, 4, 5, 6, 7)
print(data01)
print(data02)
print(data03)

# 6. 如果元组中只有一个元素,必须添加逗号
tuple04 = (10,)
print(type(tuple04))
