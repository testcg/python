"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
     提示：使用容器包装需要返回的多个数据
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""


def get_weight(total_liang):
    """
        根据总两数,计算几斤零几两.
    :param total_liang: 总两数
    :return: 元组类型(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    # 返回的是元组(只是省略了小括号)
    return jin, liang

# re = get_weight(100) # (6,4)
jin, liang = get_weight(100)
print(jin)
print(liang)
