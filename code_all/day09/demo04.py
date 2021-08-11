"""
    函数参数
        实际参数
            序列实参
            字典实参
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

list01 = [1, 2, 3]
tuple01 = (1, 2, 3)
name = "孙悟空"
func01(*list01)  # 一个容器　拆为　多个实参

dict01 = {"p2": 2, "p3": 3,"p1": 1}
func01(**dict01)
