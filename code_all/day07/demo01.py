"""
    集合set
        应用1：去重复
        基础操作
            创建
            添加
            遍历
            删除
"""
# 1. 创建
# 语法1:集合名 = {元素1, 元素2}
set01 = {"a", "b"}
# 语法2:集合名 = set(可迭代对象)
# list01 = [10, 20, 30, 20, 10, 30]
list01 = ["悟空", "八戒", "悟空", "唐僧"]
set02 = set(list01)
print(set02)

# 2. 添加
set01.add("c")

# 3. 遍历
for item in set01:
    print(item)

# 4. 删除
# set01.remove("悟空") # 如果key不存在则报错
# set01.remove("a")
set01.discard("悟空")  # 如果key不存在也不报错
print(set01)
