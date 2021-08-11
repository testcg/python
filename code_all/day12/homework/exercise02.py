"""
    5. 创建电脑类,保护数据在有效范围内
        数据:型号,   CPU型号,    内存大小,    硬盘大小
                不超过10个字符    大于0    元组长度大于等于1
"""


class Computer:
    def __init__(self, model_number="", cpu="", memory=0):
        self.model_number = model_number
        self.cpu = cpu
        self.memory = memory
        self.__hard_disk = [512,1024]

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if len(value) <= 10:
            self.__cpu = value
        else:
            raise Exception("cpu星号过长")

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        if value <= 0:
            value = 2
        self.__memory = value

    # 只读属性(先在构造函数中创建私有变量)
    @property
    def hard_disk(self):
        return self.__hard_disk

alienware = Computer("外星人ALW17M", "Intel i7", 16)
print(alienware.model_number)
alienware.cpu = "xxx"# cpu("xxx")
print(alienware.cpu)
print(alienware.memory)
print(alienware.hard_disk)
