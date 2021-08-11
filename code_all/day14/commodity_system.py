from typing import List


class CommodityModel:
    """
        学生模型：封装数据
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

    def __eq__(self, other):
        return self.cid == other


class CommodityView:
    """
        学生视图:处理界面逻辑
    """

    def __init__(self, controller):
        self.__controller = controller

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __input_commodity(self):
        cmd = CommodityModel()
        cmd.name = input("请输入商品姓名：")
        cmd.price = int(input("请输入商品单价："))
        self.__controller.add_commodity(cmd)
        print("添加成功")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for item in self.__controller.commoditys:
            # print(f"{item.name}的编号是{item.cid},单价是{item.price}")
            print(item)

    def __delete_commodity(self):
        cid = int(input("请输入商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        cmd = CommodityModel()
        cmd.cid = int(input("请输入需要修改的商品编号："))
        cmd.name = input("请输入需要修改的商品姓名：")
        cmd.price = int(input("请输入需要修改的商品单价："))
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        商品控制器：负责处理业务逻辑
    """

    __start_id = 1000

    @classmethod
    def __set_commodity_id(cls, cmd):
        cmd.cid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__commoditys = []  # type:List[CommodityModel]

    @property
    def commoditys(self):
        return self.__commoditys

    def add_commodity(self, cmd: CommodityModel):
        CommodityController.__set_commodity_id(cmd)
        self.__commoditys.append(cmd)

    def remove_commodity(self, cid: int) -> bool:
        """

        :param cid:
        :return:
        """
        if cid in self.__commoditys:
            self.__commoditys.remove(cid)
            return True
        return False

    def update_commodity(self, cmd: CommodityModel) -> bool:
        for item in self.__commoditys:
            if item.cid == cmd.cid:
                item.__dict__ = cmd.__dict__
                return True
        return False


controller = CommodityController()
view = CommodityView(controller)
view.main()
