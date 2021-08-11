"""
    列表推导式嵌套
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["牛奶", "咖啡", "雪碧", "可乐"]
# result = []
# for r in list01:
#     for c in list02:
#         result.append(r + c)
result = [r + c for r in list01 for c in list02]
print(result)
