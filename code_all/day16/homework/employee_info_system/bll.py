from typing import List

from model import EmployeeModel


class EmployeeController:
    """
        商品信息控制器
    """
    __start_id = 1001

    @classmethod
    def __set_employee_id(cls, emp):
        emp.eid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__all_employee = []  # type:List[EmployeeModel]
        self.__start_eid = 1001

    @property
    def all_employee(self):
        return self.__all_employee

    def add_employee(self, emp: EmployeeModel):
        """
            添加商品信息
        :param employee:需要添加的商品信息
        """
        EmployeeController.__set_employee_id(emp)
        self.__all_employee.append(emp)

    def remove_employee(self, eid: int) -> bool:
        """
            根据商品编号删除商品信息
        :param cid:商品编号
        :return:是否删除成功
        """
        for i in range(len(self.__all_employee)):
            if self.__all_employee[i].eid == eid:
                del self.__all_employee[i]
                return True
        return False

    def update_employee(self, commodity: EmployeeModel) -> bool:
        """
            修改商品信息
        :param commodity:商品信息
        :return:是否删除成功
        """
        for item in self.__all_employee:
            if item.eid == commodity.eid:
                item.__dict__ = commodity.__dict__
                return True
        return False
