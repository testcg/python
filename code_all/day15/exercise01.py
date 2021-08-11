"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020   9   15
    输出：星期二
"""
import time


def get_week_name(year,month,day):
    """
        获取星期名称
    :param year:年份
    :param month:月份
    :param day:天
    :return:星期名称
    """
    # "2021/03/18 11:48:56","%Y/%m/%d
    tuple_time = time.strptime(f"{year}/{month}/{day}","%Y/%m/%d")
    index = tuple_time[-3]
    list_week_name = [
        "星期一","星期二","星期三","星期四","星期五","星期六","星期日"
    ]
    return list_week_name[index]


print(get_week_name(2021,3,18))