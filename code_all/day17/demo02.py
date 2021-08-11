"""
    内置生成器
"""
list01 = [43, 43, 54, 56, 76]
# 从头到尾读          -- 读取数据方便
for item in list01:
    print(item)

# 非从头到尾读        -- 有索引能修改
for i in range(len(list01)):
    if list01[i] % 2 == 0:
        list01[i] += 1

# 读写数据时使用
for i, item in enumerate(list01):
    print(i, item)

dict01 = {"a": "A", "b": "B"}
for i, key in enumerate(dict01):
    print(i, key, dict01[key])

# for element in enumerate(list01):
#     print(element)
