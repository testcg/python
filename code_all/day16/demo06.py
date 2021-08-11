"""
    MyRange 2.0
"""
class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):

        number = 0
        yield number

        number += 1
        yield number

        number += 1
        yield number

        number += 1



# 循环一次 计算一次 返回一次
for number in MyRange(3):
    print(number)  # 0 1 2 3 4

mr = MyRange(5)
iterator = mr.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  # 0  1   2
    except StopIteration:
        break
