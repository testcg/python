# 练习1：不改变插入函数与删除函数代码，
#   为其增加验证权限的功能
def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)

    return wrapper


# insert = verify_permissions(insert)
@verify_permissions
def insert(p1):
    print("插入")
    return "ok"


@verify_permissions
def delete():
    print("删除")
    return "no"


print(insert(10))
print(delete())
