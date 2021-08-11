"""
    练习3：创建函数,根据课程阶段计算课程名称.
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("网络爬虫")
    elif number == "5":
    print("数据分析、人工智能")
"""


# def get_course_name(number):
#     if number == "1":
#         return "Python语言核心编程"
#     if number == "2":
#         return "Python高级软件技术"
#     if number == "3":
#         return "Web全栈"
#     if number == "4":
#         return "网络爬虫"
#     if number == "5":
#         return "数据分析、人工智能"


# def get_course_name(number):
#     course_name = {
#         "1": "Python语言核心编程",
#         "2": "Python高级软件技术",
#         "3": "Web全栈",
#         "4": "网络爬虫",
#         "5": "数据分析、人工智能"
#     }
#     if number in course_name:
#         return course_name[number]

def get_course_name(number):
    """

    :param number:
    :return:
    """
    course_name = [
        "Python语言核心编程",
        "Python高级软件技术",
        "Web全栈",
        "网络爬虫",
        "数据分析、人工智能"
    ]
    if 1 <= number <= len(course_name):
        return course_name[number - 1]

re = get_course_name(6)
print(re)
