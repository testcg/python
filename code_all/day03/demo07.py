"""
    真值表达式
"""
# bool(  值  )
# 为False的值：0   0.0   ""  None
# 有值则为真

if None:
    print("满足条件")

# 应用：
content = input("请输入内容：")
# if content != "":
if content: # 有值
    print(content)
else:
    print("没输入内容")
