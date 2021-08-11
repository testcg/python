from bll import StudentController
from usl import StudentView

# 如果当前是主模块,才执行入口逻辑
if __name__ == '__main__':
    controller = StudentController()
    view = StudentView(controller)
    view.main()
