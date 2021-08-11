"""
    列表基础操作list
        删除
"""
list_name = ["郭世鑫", "涛涛", "罗耀泽"]
# 1. 根据元素
list_name.remove("涛涛")
# 注意:如果元素不存在,报错
if "涛" in list_name:
    list_name.remove("涛")
# 2. 根据定位
del list_name[0]
del list_name[:]
print(list_name)
