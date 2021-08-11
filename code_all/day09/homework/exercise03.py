"""
    定义函数,根据颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
"""


def get_color(value):
    """
        根据颜色(RGBA),返回描述信息,
    :param value:颜色值
    :return:颜色的描述信息
    """
    dict_color_info = {
        "R": "红色",
        "G": "绿色",
        "B": "蓝色",
        "A": "透明度"
    }
    if value in dict_color_info:
        return dict_color_info[value]

print(get_color("A"))
