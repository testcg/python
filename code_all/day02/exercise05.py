"""
    画出下列代码内存图,说出终端显示结果
"""
name_of_beijing, region = "北京", "市"
# 拼接后成为一个独立的数据,不受原数据发生的变化影响
name_of_beijing_region = name_of_beijing + region
region = "省"
print(name_of_beijing_region)  # 北京市
del name_of_beijing
print(name_of_beijing_region)  # 北京市
