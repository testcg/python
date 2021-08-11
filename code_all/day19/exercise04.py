"""

"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # 执行旧功能
        result = func(*args, **kwargs)
        stop = time.time()
        print("执行时间：", stop - start)
        return result

    return wrapper


@print_execute_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
