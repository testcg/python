from bll import StudentController
from usl import StudentView

# 如果当前是主模块,才执行入口逻辑
if __name__ == '__main__':
    try:
        controller = StudentController()
        view = StudentView(controller)
        view.main()
    except:
        print("程序出错")
