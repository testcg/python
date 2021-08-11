"""
    索引
"""
message = "我是花果山水帘洞美猴王齐天大圣"
print(message[0])  # 我
print(message[4])  # 山
print(message[-4])  # 齐
# print(message[1.5]) # 编号必须是整数
# print(message[100]) # IndexError
# print(message[-100]) # IndexError
print(len(message))  # 字符串长度
# 通过正向索引定位最后一个元素
print(message[len(message) - 1])
# 通过反向索引定位第一个元素
print(message[-len(message)])
# 定位第三个、第五个、倒数第二个、倒数第四个
print(message[2])
print(message[4])
print(message[-2])
print(message[-4])
# 定位 "山"  "王"
print(message[4])
print(message[-5])
