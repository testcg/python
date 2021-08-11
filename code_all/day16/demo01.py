"""
    异常处理 Error
        目的：保障软件可以按照既定流程执行
"""

# 不适用以下语法错误：
# print(qtx)

# list01 = []
# print(list01[0])

# list 02 = [

# 适用于解决逻辑错误(数值超过有效范围而引起)：
"""
def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count / person_count
    print(f"每人{result}个")


div_apple(10)
"""

# 现象：不继续向下执行,而是不断向上返回
"""
def div_apple(apple_count):
    # ValueError
    person_count = int(input("请输入人数："))
    # ZeroDivisionError
    result = apple_count / person_count
    print(f"每人{result}个")

def main():
    div_apple(10)

main()

print("后续逻辑")
"""

# 写法1:包治百病(民间喜好)
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个")
    # except Exception:
    except:
        print("分苹果失败")


div_apple(10) 
"""

# 写法2:对症下药(官方建议)
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个")
    except ValueError:
        print("错误!输入的不是整数")
    except ZeroDivisionError:
        print("错误!输入的是零")

div_apple(10)
"""

# 写法3:无论是否发生错误,一定执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(f"每人{result}个")
        # 打开文件
        # 处理文件
    finally:
        print("分苹果结束啦")
        # 关闭文件

div_apple(10) 
"""


# 写法4:没有错误才执行的逻辑
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数："))
        result = apple_count / person_count
        print(f"每人{result}个")
    except:
        print("分苹果失败")
    else:
        print("分苹果成功")


div_apple(10)
print("后续逻辑")
