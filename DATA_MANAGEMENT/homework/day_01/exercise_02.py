"""
    基于单词本(dict.txt)完成一个函数
    输入单词，输入该单词的解释
"""


def word_explain(word):
    file = open("../../file/dict.txt", 'r')
    for item in file:
        tem = item.split(' ', 1)
        if tem[0] > word:
            file.close()
            break
        if word == tem[0]:
            file.close()
            return tem[1].strip()


print(word_explain('a'))
