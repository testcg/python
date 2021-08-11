"""
    列表基础操作list
        定位(读取、修改)
"""
list_name = ["郭世鑫", "刘兰涛", "罗耀泽"]
# 1. 索引 容器名[整数]
# -- 读取
print(list_name[0])
name = list_name[-1]

# -- 修改
list_name[0] = "鑫鑫"
print(list_name)

# 2. 切片 容器名[整数:整数:整数]
# -- 读取:会创建新列表执行拷贝(复制)操作
new_list = list_name[:2]
print(new_list)

# -- 修改:遍历右侧可迭代对象,依次存入左侧定位区域
list_name[-2:] = ["涛涛", "老罗"]
# 左侧定位2元素,右侧赋值0元素
# list_name[-2:] = []
# 左侧定位0元素,右侧赋值2元素
list_name[1:1] = ["tt", "ll"]
print(list_name)

# 练习3：
#     打印香港疫情信息(xx地区新增xx人现存xx人)
#     将地区列表后2个元素修改为 ["XJ","SC"]