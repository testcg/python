"""
    练习：
"""

import re

# 匹配小数
print(re.findall(r"-?[0-9]+\.[0-9]+", "12.2 2.4 -4 -6.7 8"))

# 匹配薪资
print(re.findall(r"\$\d+", "日薪：$150"))

# 匹配书名
print(re.findall("《.+?》", "《呐喊》,《python》,《罗织经》,《123~~123》"))

# 匹配IP地址
print(re.search(r"(\d{1,3}\.){3}\d{1,3}", "10.44.111.135").group())

# 匹配身份证号
print(re.search(r"(\d{17})(\d|x)", "12345678901234567x,123456789012345679").group())
