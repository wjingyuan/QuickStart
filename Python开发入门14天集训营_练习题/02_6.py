# 创建新列表[1, 2, 3, 4, 2, 5, 6, 2]，合并入names列表

names = ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', 'shanshan', 'peiqi', 'black_girl']
lst = [1, 2, 3, 4, 2, 5, 6, 2]
# new_lst = names + lst
# print(new_lst)
names.extend(lst)
print(names)
