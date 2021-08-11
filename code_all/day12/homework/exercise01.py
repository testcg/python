"""
    请以面向对象思想,描述下列情景.
        小明使用手机打电话
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        communication.dialing()


class MobilePhone:
    def dialing(self):
        print("呼叫")


xm = Person("小明")
xl = Person("小李")
xm.call(MobilePhone())
