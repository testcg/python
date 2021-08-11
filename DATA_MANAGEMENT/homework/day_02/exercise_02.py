"""
    练习：
        1.匹配大写字母开头的单词
        2.匹配一个字符串中的数字
        3.匹配一组整数，存在正数、负数
        4.匹配手机号
        5.匹配已大写字母开头的单词
"""
import re

word_01 = "Hi hello Chengeng"
print(re.findall("[A-Z][a-z]*", word_01))
word_02 = "张三：22，体重：78kg"
print(re.findall("[0-9]+", word_02))
word_03 = "100 -22 40  -25  30"
print(re.findall("-?[0-9]+", word_03))
word_04 = "我的手机号为：13659435837"
print(re.findall("1[0-9]{10}", word_04))
word_05 = "Hi I Chengeng NBA iPython"
print(re.findall(r"\b[A-Z]+[a-z]*\b", word_05))
