"""
    列表基础操作list
        创建
        添加 
"""
# 1. 创建
# 语法1：列表名 = [元素1,元素2]
list_name = ["郭世鑫", "刘兰涛", "罗耀泽"]
# 语法2:列表名 = list(可迭代对象)
list01 = list("我是孙悟空")
print(list01)
# 2. 添加
# -- 追加
list_name.append("王志振")
# -- 插入
list_name.insert(1, "秦思哲")
print(list_name)
# 练习1：
# 创建地区列表、新增列表、现有列表，至少存储3行信息
#     练习2：
#         向以上三个列表追加数据第4行数据
#         在第1个位置插入第5行数据