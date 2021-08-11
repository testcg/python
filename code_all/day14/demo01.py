"""
    Python语言变量没有类型,所以参数/列表中元素都没有类型
    优点：适合科学计算
        其他语言：
            int a = 10;
            a = 20
            a = "" # 报错
        Python
            a = 10
            a = 20
            a = ""
    缺点：没有类型,就意味着不会提示对应的操作
    解决：类型标注(注释)
        (1)语法：
            变量:类型
            def 函数名()->类型:
            self.实例变量 = 数据 # type:类型

        (2)作用:
            -- 增强代码的可读性
            -- 类型检查
            -- 提示对应的操作

        (3)复杂类型
            List, Tuple, Dict,
            Union[类型1,类型2,None],
            Optional[类型1,类型2]
"""


# 1. 对参数标注
def func01(data: int):
    print(data)


func01("a")


# 2. 对返回值进行标注
def func02() -> int:
    return 10


re = func02()
print(re)


# 3. 对实例变量
class MyClass:
    def __init__(self, data01):
        self.data01 = data01  # type:int


# 4. 复杂类型
from typing import List, Tuple, Dict, Union, Optional

# -- 容器
list01 = []  # type:List[str]
tuple01 = ("a",)  # type:Tuple[str]
dict01 = {}  # type:Dict[str,float]


# -- 标注多种类型
def func03(a: Union[int, str]):
    print(a)


# -- 可选类型(可以不传递信息)
def func04(a: Optional[int, str] = ""):
    print(a)


func04()
