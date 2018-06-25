# 循环names列表，打印每个元素的索引值和元素，当索引值为偶数时，把对应的元素改成-1

names = ['old_driver', 'rain', ['oldboy', 'oldgirl'], 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
# enumerate(list)，可以取出list中的索引号i和对应的元素x。
# 输出一般采用字典形式（i ，x）。如果希望单独输出索引和元素，可以采用如下写法。
for i,x in enumerate(names):
    if i % 2 == 0:
        names[i] = -1
print(names)