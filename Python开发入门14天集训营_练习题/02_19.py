'''
写代码，有如下元祖，请按照功能要求实现每一个功能。
tu = ('alex', 'eric', 'rain')
1. 计算元祖长度并输出
2. 获取元祖的第2个元素并输出
3. 获取元祖的第1-2个元素并输出
4. 请使用for输出元祖的元素
5. 请使用for、len、range输出元祖的索引
6. 请使用enumerate输出元祖元素和序号（序号从10开始）
'''

tu = ('alex', 'eric', 'rain')
print(tu)

# 1. 计算元祖长度并输出
print('第1题：计算元祖长度并输出')
length = len(tu)
print('元祖的长度为：%d \n' % length)

# 2. 获取元祖的第2个元素并输出
print('第2题：获取元祖的第2个元素并输出')
print('元祖的第2个元素为：%s \n' % tu[1])

# 3. 获取元祖的第1-2个元素并输出
print('第3题：获取元祖的第1-2个元素并输出')
answer = tu[:2]
print('元祖的第1-2个元素为：{} \n'.format(answer))  # 用%s代替tu[:2]为什么不行？因为切片后有2个元素。
# print('元祖的第1-2个元素为：%s%s \n' % answer)

# 4. 请使用for输出元祖的元素
print('第4题：请用for输出元祖的元素')
for i in tu:
    print(i, end = ' ')
    print()

# 5. 请使用for、len、range输出元祖的索引
print('第5题：请使用for、len、range输出元祖的索引')
for i in range(len(tu)):
    print('%s的索引是：%d' % (tu[i], i))

# 6. 请使用enumerate输出元祖元素和序号（序号从10开始）
print('第6题：请使用enumerate输出元祖元素和序号（序号从10开始）')
for index, j in enumerate(tu):
    print(index + 10, j)