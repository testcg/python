"""
    write(data)
    功能: 把文本数据或二进制数据块的字符串写入到文件中去
    参数：要写入的内容
    返回值：写入的字符个数
"""
"49:39"

file = open("../file/file_01.txt", 'a+', encoding='utf-8')
word_01 = "中国共产党成100周年\n"
file.write(word_01)
"""
    writelines(str_list)
    功能：接受一个字符串列表作为参数，将它们写入文件。
    参数: 要写入的内容列表
"""
word_02 = ["出师表\n", "先帝创业维伴儿中道崩殂"]
file.writelines(word_02)
file.close()
