"""
    for + range
"""
# 写法1:range(开始,结束,间隔)
# 不包含结束值
for item in range(3, 8, 1):
    print(item)  # 3 4 5 6 7

# 写法2:range(开始,结束)
# 间隔默认为1
for item in range(3, 8):
    print(item)  # 3 4 5 6 7

# 写法3:range(结束)
# 开始默认为0
for item in range(5):
    print(item)  # 3 4 5 6 7
