"""
    多函数互相调用
"""


# ------------定义函数----------------
def repeat_attack(count): # 2
    result = []
    for __ in range(count):
         result.append(attack())
    return result

def attack(): # 3
    print("直拳")
    print("摆拳")
    print("勾拳")
    return "ok"

# ------------调用函数----------------
print(repeat_attack(2))# 1 
