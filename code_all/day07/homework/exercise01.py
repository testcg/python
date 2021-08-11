"""
    在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
"""
color_value = input("请输入颜色编号(RGBA):")
dict_color_info = {
    "R": "红色",
    "G": "绿色",
    "B": "蓝色",
    "A": "透明度"
}
if color_value in dict_color_info:
    print(dict_color_info[color_value])
else:
    print("输入的颜色不存在")
