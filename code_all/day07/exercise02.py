"""
    ******
    ######
    ******
    ######
"""
# 4    6
for r in range(4):  # 0     1     2     3
    for c in range(6):
        if r % 2 == 0:
            print("*", end="")
        else:
            print("#", end="")
    print()
