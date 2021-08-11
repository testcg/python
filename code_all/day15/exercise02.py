"""
    练习2：定义函数,根据生日(年月日),计算活了多天.
    输入：2010   1   1
    输出：从2010年1月1日到现在总共活了3910天
"""
import time


def get_life_days(year, month, day):
    """
        根据生日计算活的天数
    :param year:年份
    :param month:月份
    :param day:天
    :return:天数
    """
    tuple_time = time.strptime(f"{year}/{month}/{day}", "%Y/%m/%d")
    life_second = time.time() - time.mktime(tuple_time)
    return life_second / 24 / 60 / 60


print("%.2f" % get_life_days(1995, 9, 25))
