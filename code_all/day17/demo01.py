"""
    MyRange 1.0  迭代器实现
        day16/exercise04.py
    MyRange 2.0  迭代器 --> yield
        day16/demo06.py
    MyRange 3.0  yield --> 生成器
"""


# 价值：循环一次  计算一次  返回一次
def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1


for number in my_range(5):
    print(number)  # 0 1 2 3 4

# 调用但不执行函数体,而是返回生成器对象
# mr = my_range(5)
# iterator = mr.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)  # 0  1   2
#     except StopIteration:
#         break


"""
class generator: # 生成器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        index += 1
        return index
"""
