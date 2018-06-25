# names里有3个2，请返回第2个2的索引值。不要人肉数，要动态查找（提示：找到第一个2的位置，在此基础上再查找第2个）

names = ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
i_1 = names.index(2)
i_2 = i_1 + 1
child_names = names[i_2 : ]
i_3 = child_names.index(2)
i_4 = i_1 + i_3 + 1
print('第2个2的索引值为{}：'.format(i_4))