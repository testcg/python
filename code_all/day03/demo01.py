"""
    变量交换
"""
bridegroom_name = "武大郎"
bride_name = "潘金莲"
# 传统思想：借助第三方变量
# temp = bridegroom_name
# bridegroom_name = bride_name
# bride_name = temp
# 交换律思想：a,b=b,a
bridegroom_name, bride_name = bride_name, bridegroom_name
print("交换后的新郎：" + bridegroom_name)
print("交换后的新娘：" + bride_name)
