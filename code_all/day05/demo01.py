"""
    索引
        定位单个元素
        容器名[整数]
    切片
        定位多个元素
        容器名[开始:结束:间隔]
"""
message = "我是花果山水帘洞美猴王齐天大圣"
# 写法1：容器名[开始:结束:间隔]
# 注意：不包含结束
print(message[2:5:1])  # 花果山
# 写法2：容器名[开始:结束]
# 注意：间隔默认为1
print(message[2:5])  # 花果山
# 写法3：容器名[:结束]
# 注意：开始默认为开头
print(message[:5])  # 花果山
# 写法4：容器名[开始:]
# 注意：结束默认为尾巴
print(message[-4:])  # 齐天大圣
print(message[:])# 我是花果山水帘洞美猴王齐天大圣
# 特殊：翻转
print(message[::-1])# 圣大天齐王猴美洞帘水山果花是我
# 花果山水帘洞美猴王
print(message[2:-4])
# 王猴美洞帘水山果花
# print(message[-5:1])# 空
print(message[-5:1:-1])
# 不怕越界
print(message[2:100])# 花果山水帘洞美猴王齐天大圣
print(message[1:1]) # 空
print(message[::2]) # 我花山帘美王天圣