import re

"""
    匹配字符重复
    元字符: *
    匹配规则：匹配前面的字符出现0次或多次
"""
re_01 = re.findall("ab*", "abbacabbba")
# print(re_01)

"""
    元字符：+
    匹配规则： 匹配前面的字符出现1次或多次
"""
re_02 = re.findall("ab+", "abbacabbba")
# print(re_02)

"""
    元字符：?
    匹配规则： 匹配前面的字符出现0次或1次
"""
re_03 = re.findall("ab?", "abbacabbba")
# print(re_03)

"""
    元字符：{n}
    匹配规则： 匹配前面的字符出现n次
"""
re_04 = re.findall("ab{3}", "abbacabbba")
print(re_04)

"""
    元字符：{m,n}
    匹配规则： 匹配前面的字符出现m-n次
"""
re_05 = re.findall("ab{1,3}", "abbacabbba")
print(re_05)
