"""
    匹配任意（非）数字字符
    元字符： \d \D
    匹配规则：\d 匹配任意数字字符，\D 匹配任意非数字字符
"""
import re

word_01 = "http://10.44.111.98:8282/hwsfstation/core/base/home"
re_01 = re.findall("\d{1,4}", word_01)
re_02 = re.findall("\D+", word_01)
print(re_01, re_02)

"""
    匹配任意（非）普通字符
    元字符： \w \W
    匹配规则: \w 匹配普通字符，\W 匹配非普通字符
    说明: 普通字符指数字，字母，下划线，汉字。
"""
re_03 = re.findall("\W+", word_01)
re_04 = re.findall("\w+", word_01)
print(re_03, re_04)

"""
    匹配任意（非）空字符
    元字符： \s \S
    匹配规则:\s匹配空字符，\S 匹配非空字符
    说明：空字符指 空格\r \n \t \v \f 字符
"""

re_05 = re.findall('\w+\s+\w+', "hello    world")
re_06 = re.findall('\w+\S+\w+', "hello    world")
print(re_05, re_06)

"""
    匹配（非）单词的边界位置
    元字符：\b \B
    匹配规则：\b 表示单词边界，\B 表示非单词边界
    说明：单词边界指数字字母(汉字)下划线与其他字符的交界位置。
"""

re_07 = re.findall(r'\bis\b', "This is a test.")
re_08 = re.findall(r'\Bis', "This is a test.")
print(re_07, re_08)
