"""
    重写内置函数 - 增强运算符
        算数运算符,返回新数据
        增强运算符,返回原数据

        在函数中，需要判断参数的类型，使用关系判断(isinstance,issubclass,type)
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x的分量是:{self.x},y分量{self.y}"

    # + 返回新数据
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # += 返回原对象
    def __iadd__(self, other):
        # 传入的是向量
        if type(other) == Vector2:
            self.x += other.x
            self.y += other.y
        else:  # 否则
            self.x += other
            self.y += other
        return self


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos01 += pos02  # pos01.__iadd__(pos02)
print(pos01)

pos01 += 10  # pos01.__iadd__(10)
print(pos01)

"""
# += 可变对象,在原有基础上修改
list01 = [10]
print(id(list01))  # 140198763634568
list01 += [20]
print(id(list01))  # 140198763634568
# += 不可变对象,会创建新对象
tuple01 = (10,)
print(id(tuple01))  # 140646377164136
tuple01 += (20,)
print(id(tuple01))  # 140646346682504
"""
