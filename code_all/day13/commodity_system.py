class CommodityModel:
    """
        学生模型：封装数据
    """

    def __init__(self, name="", price=0, sid=0):
        self.name = name
        self.price = price
        self.sid = sid


class CommodityView:
    """
        学生视图:处理界面逻辑
    """

    def __init__(self, controller):
        self.controller = controller

    def display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.input_commodity()
        elif item == "2":
            pass

    def input_commodity(self):
        cmd = CommodityModel()
        cmd.name = input("请输入商品姓名：")
        cmd.price = int(input("请输入商品单价："))
        self.controller.add_commodity(cmd)
        print("添加成功")


class CommodityController:
    """
        学生控制器：负责处理业务逻辑
    """

    def add_commodity(self, cmd):
        pass


controller = CommodityController()
view = CommodityView(controller)
while True:
    view.display_menu()
    view.select_menu()
