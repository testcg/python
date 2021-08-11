"""
    练习2：画出下列内存图
""" 
list01 = ["北京", "上海", "深圳"]
list02 = list01
list01.insert(0,"天津")
del list01[1]
print(list02)# ?