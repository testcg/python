def rank(*args):
    list_target = list(args)
    for i in range(len(list_target) - 1):
        for j in range(i + 1, len(list_target)):
            if list_target[i] > list_target[j]:
                list_target[i], list_target[j] = list_target[j], list_target[i]
    return tuple(list_target)


print(rank(2, 3, 1, 5))
print(rank(*[2, 3, 1, 5]))
