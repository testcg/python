"""
    请以容器思想（统一管理数据）,改造下列代码.
    month = int(input("请输入月份："))
    if 1 <= month <= 12:
        if month == 2:
            print("28天")
        elif month == 4 or month == 6 or month == 9 or month == 11:
            print("30天")
        else:
            print("31天")
    else:
        print("月份有误")
"""
month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        print("28天")
    elif month in (4, 6, 9, 11):
        print("30天")
    else:
        print("31天")
else:
    print("月份有误")

# 将每月天数存入容器
# day = 29 if 闰年条件 else 28
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# 5月份天数
print(day_of_month[4])
