"""
    练习1：创建计算治愈比例的函数
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")
"""


def calculate_cure_rate(confirmed, cure):
    """
        计算治愈比例
    :param confirmed: 确诊人数
    :param cure: 治愈人数
    :return: 治愈比例
    """
    cure_rate = cure / confirmed * 100
    return cure_rate


re = calculate_cure_rate(56, 50)
print("%.2f" % re)
