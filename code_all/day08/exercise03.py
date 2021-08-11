"""
    练习2：创建函数,在终端中打印矩形.
    number = int(input("请输入整数:"))  # 5
    for row in range(number):
        if row == 0 or row == number - 1:
           print("*" * number)
      else:
            print("*%s*" % (" " * (number - 2)))
"""


# 崇尚小而精,拒绝大而全
def print_rectangular(number, character):
    """
        在终端终端打印矩形
    :param number: 整数类型的边长
    :param character: 字符串类型的填充字符
    """
    for row in range(number):
        if row == 0 or row == number - 1:
            print(character * number)
        else:
            print(character + " " * (number - 2) + character)

# num = int(input("请输入整数:"))
# num = 5
# print_rectangular(num)
print_rectangular(8, "*")
print_rectangular(4, "#")
