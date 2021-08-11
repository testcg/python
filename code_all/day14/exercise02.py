"""
    练习1：
    创建2个模块module_exercise.py与exercise.py
        将下列代码粘贴到module_exercise模块中，并在exercise中调用。
"""
# 方式1
# 更适合面向过程(全局变量、函数)
import module_exercise

print(module_exercise.data)
module_exercise.func01()
module_exercise.MyClass.func03()
obj = module_exercise.MyClass()
obj.func02()

# 方式2:
# 更适合面向对象(类)
from module_exercise import data, func01, MyClass

print(data)
func01()
MyClass.func03()
obj = MyClass()
obj.func02()
