"""
    列表内存图
        定位内存图
"""
list01 = [10,20,30]
data01 = list01
data02 = list01[0]
data03 = list01[:2]

list01[0] = 100
list01[:2] = [1000,2000]

print(list01)
print(data01)
print(data02)
print(data03)