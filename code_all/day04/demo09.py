"""
    通用操作
        算数运算符
"""
name01 = "悟空"
name02 = "八戒"
# 拼接两个容器元素
name03 = name01 + name02
print(name03)  # 悟空八戒

# 重复容器中的元素
name04 = name01 * 20
print(name04)  # 悟空悟空

# 依次比较两个容器中元素,一但不同则返回比较结果。
print(name01 > name02)

# 成员运算符
# True
print("悟空" in "花果山水帘洞齐天大圣孙悟空")
print("水帘" in "花果山水帘洞齐天大圣孙悟空")
# False
print("大圣齐天" in "花果山水帘洞齐天大圣孙悟空")
print("水洞" in "花果山水帘洞齐天大圣孙悟空")
