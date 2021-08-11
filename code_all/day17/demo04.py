"""
    列表推导式
        列表 = [对变量操作 for 变量 in 可迭代对象]
        列表 = [对变量操作 for 变量 in 可迭代对象 if 条件]
        优点：
            可以定位(索引切片)
            反复使用
        缺点：
            占用内存

    生成器表达式
        生成器 = (对变量操作 for 变量 in 可迭代对象)
        生成器 = (对变量操作 for 变量 in 可迭代对象 if 条件)
        优点：
            节省内存
        缺点：
            不可以定位(索引切片)
            不反复使用
"""
list01 = [432, 5, 54, 6, 76, 87]
# 需求：将大于10的元素存储新列表
list02 = [item for item in list01 if item > 10]
for item in list02:
    print(item)

generator02 = (item for item in list01 if item > 10)
for item in generator02:
    print(item)
