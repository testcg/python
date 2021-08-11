"""
    for for
"""

"""
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行

print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行
"""

"""
for c in range(5): # 0 1 2 3 4
    print("*", end=" ")
print() # 换行

for c in range(5): # 0 1 2 3 4
    print("*", end=" ")
print() # 换行
"""

# 外层循环执行1次,内层循环执行多次
for r in range(2):#       0        1
    for c in range(5): #01234    01234
        print("*", end=" ")
    print() # 换行

"""
******
######
******
######
"""
