"""
练习7：创建函数,根据年月日计算这是这一年的第几天.
        如果2月是闰年,按29天计算
        　　　    平年   28
month = int(input("请输入月:"))
day = int(input("请输入日:"))
days_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_days = sum(days_of_month[:month - 1])
total_days += day
print(f"{month}月{day}日是第{total_days}天.")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28
"""
def sum_day(year,month,day):# 2
    day_of_month02 = get_day_by_month02(year)
    days_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    return total_days

def get_day_by_month02(year):# 3
    # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #     return 29
    # else:
    #     return 28
    return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28

print(sum_day(2021, 3, 9))# 1