"""
    汇率转换器
"""
# 1. 获取数据（美元）
usd = float(input("请输入美元："))
# 2. 逻辑计算（美元 × 6.473）
cny = usd * 6.473
# 3. 显示结果（1美元=6.473人民币）
print(str(usd) + "美元=" + str(cny) + "人民币")
