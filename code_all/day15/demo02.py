"""
    标准库模块 - time
"""
import time

# 1. 人类时间(时间元组)：    　公园元年～2021年3月18日
#          　　　　　-221
# (年,月,日,时,分,秒,星期,年的第几天,是否是夏令时)
tuple_time = time.localtime()
print(tuple_time[3])  # 时
print(tuple_time.tm_hour)  # 时
print(tuple_time[-3])  # 星期
print(tuple_time.tm_wday)  # 星期
print(tuple_time[:3])  # 年,月,日

# 2. 机器时间(时间戳): 1970年元旦～现在经过的秒数
# 1616037532.2794447
# 1616037713.6778865
print(time.time())

# 3. 时间戳->时间元组
# 语法:时间元组 = time.localtime( 时间戳 )
print(time.localtime(1616037532.2794447))
# 4. 时间元组-> 时间戳
# 语法:时间戳 = time.mktime(9个元素的元组)
print(time.mktime((2021, 3, 18, 11, 34, 30, 0, 0, 0)))
print(time.mktime(tuple_time))

# 5. 时间元组->字符串
# 语法：字符串 = time.strftime("格式", 时间元组)
# 21/03/18 11:49:02
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
# 2021/03/18 11:48:56
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("年份:%Y,月份:%m,天:%d %H:%M:%S", tuple_time))

# 6. 字符串->时间元组
# 语法：时间元组 = time.strptime(时间字符串,格式)
time.strptime("2021/03/18 11:48:56","%Y/%m/%d %H:%M:%S")
print(time.strptime("11:48:56","%H:%M:%S"))
# print(time.strptime("11-48-56","%H:%M:%S"))
# print(time.strptime("11:48","%H:%M:%S"))
