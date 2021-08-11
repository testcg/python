"""
    小结 - 容器
        1. 种类与特点
            字符串str:存储字符编码,不可变,序列
            列表list:存储变量,可变,序列
            元组tuple:存储变量,不可变,序列
            字典dict:存储键值对,可变,散列
                键必须唯一且不可变(数值、字符串、元组、bool...)
            集合set:存储键,可变,散列

        2. 可变与不可变
            可变:预留空间 + 自动扩容
            不可变:按需分配
        3. 序列与散列
            序列：有顺序,空间连续,定位元素灵活(支持索引切片)
            散列：无顺序,分散存储,定位单个元素最快,代码可读性更高(key的名字可以自定义)
"""
# 1. 创建
list01 = [10, 20, 30]
dict01 = {"a": 10, "b": 20, "a": 30}
print(dict01)  # {'a': 30, 'b': 20}

# 2. 添加
list01.append(40)
list01.insert(0, 40)

dict01["c"] = 40

# 3. 定位
print(list01[:2])  # 前两个元素
print(list01[-2:])  # 后两个元素

print(dict01["b"])

# print(list01[99]) # 索引越界
# print(dict01["x"])  # 键不存在

# 4. 遍历
for item in list01:
    print(item)

for i in range(len(list01) - 1, -1, -1):
    print(list01[i])

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for key, value in dict01.items():
    print(key)
    print(value)

# 5. 删除
del list01[1]
list01.remove(30)

del dict01["a"]

# 不支持遍历字典时删除字典记录
# for key,value in dict01.items():
#     if value == 20:
#         del dict01[key]

# 遍历列表(所有key)时删除字典记录
for key in list(dict01):
    if dict01[key] == 20:
        del dict01[key]
print(dict01)
