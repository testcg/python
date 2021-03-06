"""
    总结 - 面向对象
        字面意思：考虑问题从对象的角度出发
                谁?干嘛?
        三大特征：
            封装(分)：将大的需求划分为多个类型
                创建人类,汽车,飞机类
            继承(隔)：将相关概念的共性进行抽象、统一操作
                创建交通工具隔离人类与汽车飞机等类的变化
            多态(做)：以重写的方式实现子类的个性
                汽车,飞机重写交通工具的运输方法

        价值：满足开闭原则(增加新变化点,客户端代码不变)
                增加轮船、自行车,人类不需要改变
        语法：
            class 类名:
                类变量 = 数据

                @classmethod
                def 类方法(cls):
                    操作类变量

                def __init__(self,参数):
                    self.实例变量 = 参数

                def 实例方法(self):
                    操作实例变量

            对象 = 类名(数据)
            对象.实例变量  # 每个对象一份  [自己]
            对象.实例方法()

            类名.类变量   # 所有对象一份  [大家]
            类名.类方法()
"""
