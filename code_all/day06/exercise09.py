"""
    练习1：
    将两个列表，合并为一个字典
            姓名列表["张无忌","赵敏","周芷若"]
            房间列表[101,102,103]
    {101: '张无忌', 102: '赵敏', 103: '周芷若'}
    练习2：
    颠倒练习1字典键值
    {'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]
# result = {}
# for i in range(len(list_name)):
#     key = list_room[i]
#     value = list_name[i]
#     result[key] = value
result = {list_name[i]: list_room[i] for i in range(len(list_name))}
print(result)

# new_result = {}
# for key, value in result.items():
#     new_result[value] = key
new_result = {value: key for key, value in result.items()}
print(new_result)
