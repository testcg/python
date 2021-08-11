"""
    求10000以内素数的和
"""


def is_prime(num):
    if num <= 1:
        return False
    for item in range(2, num // 2 + 1):
        if num % item == 0:
            return False
    else:
        return True


result = 0
for item_ in range(10000):
    if is_prime(item_):
        result += item_
print(result)
