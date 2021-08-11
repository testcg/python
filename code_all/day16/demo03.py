"""
    可迭代对象
        迭代 iteration：重复获取下一个元素的过程
        迭代器 iterator：执行迭代过程的对象
        可迭代 iterable：可以创建迭代器的对象
"""
message = "我是花果山水帘洞孙悟空"
# for item in message:
#     print(item)

# for 循环原理
# 1. 获取迭代器对象
iterator = message.__iter__()
# 2. 获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
        # 3. 如果停止迭代则跳出循环
    except StopIteration:
        break
# 面试题：
# 能够参与for循环的条件是什么?
