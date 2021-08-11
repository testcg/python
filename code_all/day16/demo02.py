"""
    人为创造异常
        目的：快速传递错误消息
"""


class Wife:
    def __init__(self, age=0):
        self.age = age  # 2

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 80:  # 3
            self.__age = value
        else:
            # 人为创造异常　　"发送"
            raise Exception("我不要")


while True:
    try: # "接收"
        jn = Wife(int(input("请输入年龄：")))  # 1
        print(jn.age)
        break
    except Exception as e:
        print(e.args)
        print("年龄超过有效范围")