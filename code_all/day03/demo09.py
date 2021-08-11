"""
    while 循环
        当满足条件时执行循环体
        执行后再判断条件,如果还满足则继续执行...

        while True:
            循环体
            if 退出条件:
                break # 跳出循环
"""
while True:
    number = int(input("请输入数字："))
    if number > 0:
        print("正数")
    elif number < 0:
        print("负数")
    else:
        print("零")

    if input("请输入q键退出:") == "q":
        break
