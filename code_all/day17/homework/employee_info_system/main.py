from bll import EmployeeController
from usl import EmployeeView

if __name__ == '__main__':
    view = EmployeeView(EmployeeController())
    view.main()
