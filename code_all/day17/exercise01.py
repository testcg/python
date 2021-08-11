# 练习1：定义函数,在列表中找出所有偶数
# [43,43,54,56,76,87,98]
# -- 传统思想：创建容器存储所有偶数,return容器
# -- 生成器思想：一个个推算偶数,yield 偶数

def get_evens1(list_number):
    result = []
    for item in list_number:
        if item % 2 == 0:
            result.append(item)
    return result

def get_evens2(list_number):
    for item in list_number:
        if item % 2 == 0:
            yield item

list01 = [43, 43, 54, 56, 76, 87, 98]
re = get_evens1(list01)
for item in re:
    print(item)

list01 = [43, 43, 54, 56, 76, 87, 98]
re = get_evens2(list01)
for item in re:
    print(item)
