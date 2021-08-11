"""
    实例成员
        对象.成员名

        实例变量
            对象.变量名 = 数据
        实例方法
            def 方法名(self,参数):
                函数体

            对象.方法名(数据)
"""

name = "建宁"

class Wife:
    def __init__(self, name=""):
        # 创建实例变量
        self.name = name

    # 实例方法
    def play(self):
        print(self.name + "在玩耍")


w01 = Wife("丽丽")
# 修改实例变量
w01.name = "莉莉"
# 读取实例变量
print(w01.name)
# 系统自带的__dict__变量,存储着对象所有实例变量{'name': '莉莉'}
print(w01.__dict__)  # {'name': '莉莉'}

w01.play()  # play(w01)
Wife.play(w01) # 通过类名调用实例方法,必须自行添加对象

# 不建议在类外创建实例变量
"""
class Wife:
    pass

w01 = Wife()
# 创建实例变量
w01.name = "莉莉"
# 读取实例变量
print(w01.name)
"""

# 不建议在__init__外创建实例变量
"""
class Wife:
    def set_name(self, name):
        self.name = name


w01 = Wife()
# 创建实例变量
w01.set_name("莉莉")
# 读取实例变量
print(w01.name)
"""
