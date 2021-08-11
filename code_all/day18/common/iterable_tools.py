"""
    可迭代对象工具集
    1. 教学目的：学习函数式编程思想（分隔做）
    2. 实用角度：日积月累,功能无限壮大
    3. 面试技巧：精通函数式编程,
               运用函数式编程思想,创建了集成操作框架
               (来源于微软Linq技术)
"""


class IterableHelper:
    """
        可迭代对象助手类
        集成操作框架
    """
    # 静态方法：不需要操作实例与类成员
    # 语义：工具函数(常用且独立)
    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中,根据任意条件查找满足的所有元素
        :param iterable:可迭代对象
        :param condition:函数类型,查找条件
        :return:生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def find_single(iterable,condition):
        """
            在可迭代对象中,根据任意条件查找满足的单个元素
        :param iterable:可迭代对象
        :param condition:函数类型,查找条件
        :return:生成器,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def select(iterable,condition):
        """
            在可迭代对象中,根据逻辑处理元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的处理逻辑
        :return:生成器,推算处理结果
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def get_count(iterable,condition):
        """
            在可迭代对象中计算满足条件的元素数量
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def sum(iterable,condition):
        """
            在可迭代对象中根据条件累计运算
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:累计结果
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)
        return sum_value
