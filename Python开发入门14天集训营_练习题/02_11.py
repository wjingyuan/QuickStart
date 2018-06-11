# 循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成-1

names = ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
for index, i in enumerate(names):
    while index % 2 == 0:
        names[index] = -1
    print(index, i)