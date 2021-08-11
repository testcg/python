"""
    面向对象
        字面意思：考虑问题从对象的角度出发
                谁？在干嘛？
        作用：以人的思维方式，解决软件工程问题
                找人干活
        流程：客观事物-抽象化->类(模板)-具体化->对象
        语法：
            class 类名:
                类变量名 = 数据   # 多个对象相同数据 [饮水机]

                @classmethod
                def 类方法名(cls):
                    ...

                def __init__(self,参数):
                    self.实例变量 = 参数  # 多个对象不同数据 [杯子]

                def 实例方法(self,参数):
                    ...

            对象名 = 类名(数据)
            对象名.实例变量
            对象名.实例方法(数据)

            类名.类变量名
            类名.类方法名()
"""
message = str("我是孙悟空")
# 调用字符串对象的实例方法
num = message.count("空")
print(num)