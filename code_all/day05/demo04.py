"""
    列表基础操作list
        遍历
"""
list_name = ["郭世鑫", "涛涛", "罗耀泽"]
# 1. 从头到尾读取
for item in list_name:
    print(item)

# 2. 非从头到尾读取
# 需求：将姓名是2个字的人名改为空字符串
# -- 修改
for i in range(len(list_name)):
    if len(list_name[i]) == 2:
        list_name[i] = ""

# 需求：非从尾到头读取(一行一个)
# 因为切片会创建新(拷贝)列表,浪费内存
# for item in list_name[::-1]:# 2 1 0
#     print(item)
# 开始:len(列表名)-1  最后一个索引
# 结束:-1 因为range不包含结束只,所以实际取到的是0
# 间隔:-1 倒序
for i in range(len(list_name) - 1, -1, -1):  # 2 1 0
    print(list_name[i])

# 开始:len(列表名)-1  最后一个元素
# 结束:-1 定位最后一个元素
# for item in list_name[len(list_name) - 1:-1:-1]:# 2 1 0
#     print(item)
