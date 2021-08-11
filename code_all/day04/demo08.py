"""
    字符串字面值
"""
# 1. 各种写法
content01 = "字面值"
content02 = '字面值'
# 可见即所得
content03 = '''字面值'''
content03 = """
字
    面
值"""
print(content03)

# 2. 引号冲突
content04 = '我是"孙悟空"。'
content05 = "我是'孙悟空'。"
content06 = """我是'孙'悟"空"。"""

# 3. 转义符:改变原始含义的特殊字符
# \"  \'   \\   \n换行  ...
content07 = "我是\"孙悟空\"。"
content08 = "我是\n孙悟空。"
url = "c:\\a\\b\c\d.txt"
# 原始字符 r"字符串"
url = r"c:\a\b\c\d.txt"
print(content08)

# 4. 字符串格式化
subject = "I"
predicate = "kiss"
object = "you"
# print("主语是:" + subject + ",谓语是:" + predicate + ",宾语是:" + object + ".")
print("主语是:%s,谓语是:%s,宾语是:%s." % (subject, predicate, object))

cure_rate = 99.5
# print("治愈比例为" + str(cure_rate) + "%")
print("治愈比例为%s%%" % (cure_rate))

# %f 用于控制小数精度
money = 1.23245124
print("金额是:%.2f元" % money) # 金额是:1.23元

# %d 用于控制整数位数
second = 6
print("秒：%.2d"%(second)) #秒：06

