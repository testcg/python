"""
    练习3：
        在终端中循环录入5个成绩,
        最后打印平均成绩(总成绩除以人数)
        效果：
        请输入成绩：98
        请输入成绩：83
        请输入成绩：90
        请输入成绩：99
        请输入成绩：78
        平均分：89.6
"""
count = 0
total_score = 0
while count < 5:
    count += 1
    total_score += int(input("请输入成绩："))
print("平均分：" + str(total_score / 5))
