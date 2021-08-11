import re

"""
    普通字符
    匹配规则：每个普通字符匹配其对应的字符
"""
re_01 = re.findall("ab", "abcdefgababab")
re_02 = re.findall("陈庚", "陈庚陈赓")
# print(re_01, re_02)

"""
    或关系
    元字符: |
    匹配规则: 匹配 | 两侧任意的正则表达式即可
"""
re_03 = re.findall("ab|ca", "abcabc")
# print(re_03)

"""
    匹配单个字符
    元字符：.
    匹配规则：匹配除换行外的任意一个字符
"""
re_04 = re.findall("张.丰", "张三丰,张四丰,张五丰,张丰,张六丰")
# print(re_04)

"""
    匹配字符集
    元字符： [字符集]
    匹配规则: 匹配字符集中的任意一个字符
    表达形式:
    [abc#!好] 表示 [] 中的任意一个字符 [0-9],[a-z],[A-Z] 表示区间内的任意一个字符 [_#?0-9a-z] 混合书写，一般区间表达写在后面
"""
re_05 = re.findall('[abcde]', "How are you?")
re_06 = re.findall('[A-Z]', "How are you?")
re_07 = re.findall('[a-z]', "How are you?")
re_08 = re.findall('[ ?a-z]', "How are you?")
# print(re_05, re_06, re_07, re_08)

"""
    匹配字符集反集
    元字符：[^字符集]
    匹配规则：匹配除了字符集以外的任意一个字符
"""

re_09 = re.findall('[^A-Z]', "How are you?")
re_10 = re.findall('[^ ]', "How are you?")
# print(re_09, re_10)

"""
    匹配字符串开始位置
    元字符: ^
    匹配规则：匹配目标字符串的开头位置
"""
re_11 = re.findall('^How', "How are you?")
# print(re_11)

"""
    匹配字符串的结束位置
    元字符: $
    匹配规则: 匹配目标字符串的结尾位置
"""
re_12 = re.findall('you\?$', "How are you?")
print(re_12)

