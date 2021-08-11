"""
    练习：
    循环录入编码值打印文字，直到输入空字符串停止。
"""
while True:
    str_number = input("请输入编码值：")
    if str_number == "":
        break
    print(chr(int(str_number)))
