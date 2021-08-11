"""
    猜数字2.0
        最多猜3次,3次以内提示"恭喜猜对了"
                     外     游戏失败
"""
import random

random_number = random.randint(1, 100)
count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了,总共猜了" + str(count) + "次。")
        # break
else:# 如果循环从break结束,不执行else语句
    print("游戏失败")