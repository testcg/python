"""
    函数式编程 - 应用
        适用性：
            多个函数主体逻辑相同,但核心算法不同
        思想(步骤)：
            "封装":将变化点【分】为多个函数
                例如:condition01、condition02、
            "继承":将变化点【抽象】为参数,
                  通过参数确定【统一】的调用方法,
                  从而【隔离】通用函数与变化点函数
                例如：condition
            "多态"：编通用函数时调用参数
                   运行时传递变化点函数
            价值：增加新变化点函数,不影响通用函数
"""
list01 = [342, 4, 54, 56, 6776]


# 定义函数,在列表中查找所有大于100的数
def get_number_gt_100():
    for number in list01:
        if number > 100:
            yield number


# 定义函数,在列表中查找所有偶数
def get_number_by_even():
    for number in list01:
        if number % 2 == 0:
            yield number

# 参数：得到的是列表中的元素
# 返回值：对列表元素判断后的结果(True False)
def condition01(number):
    return number > 100

def condition02(number):
    return number % 2 == 0

# 通用函数
def find_all(condition): # 抽象
    for item in list01:
        # if number > 100:
        # if condition01(item):
        # if condition02(item):
        if condition(item):# 统一
            yield item

# 变化点函数：查找小于10的数据
def condition03(number):
    return number < 10

for item in find_all(condition03):
    print(item)













