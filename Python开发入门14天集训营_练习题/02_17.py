'''
写代码，有如下列表，按照要求实现每一个功能。
li = ['alex', 'eric', 'rain']
1. 计算列表长度并输出
2. 列表中追加元素“Tony”,并输出添加后的列表
3. 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
4. 请删除列表中的元素“eric”，并输出修改后的列表
5. 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
6. 请删除列表中的第3个元素，并输出删除元素后的列表
7. 请删除列表中的第2至4个元素，并输出删除元素后的列表
8. 请将列表所有的元素反转，并输出反转后的列表
9. 请使用for、len、range输出列表的索引
10. 请使用enumarate输出列表元素和序号（序号从100开始）
11. 请使用for循环输出列表的所有元素
'''

# 1. 计算列表长度并输出
print('第1题：')
li = ['alex', 'eric', 'rain']
length = len(li)
print('%s的长度为：%d' % (li, length))

# 2. 列表中追加元素“Tony”,并输出添加后的列表
print('第2题：')
li = ['alex', 'eric', 'rain']
li.append('Tony')
print(li)

# 3. 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
print('第3题：')
li[1] = 'Kelly'
print(li)

# 4. 请删除列表中的元素“eric”，并输出修改后的列表
print('第4题：')
li = ['alex', 'eric', 'rain']
print('原列表为：%s' % li)
li.remove('eric')
print('新列表为：%s' % li)

# 5. 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print('第5题：')
li = ['alex', 'eric', 'rain']
answer = li[1]
li.remove(answer)
print(answer)
print(li)

# 6. 请删除列表中的第3个元素，并输出删除元素后的列表
print('第6题：')
li = ['alex', 'eric', 'rain']
li.pop()
print(li)

# 7. 请删除列表中的第2至3个元素，并输出删除元素后的列表
print('第7题：')
li = ['alex', 'eric', 'rain']
del li[1:]
print(li)

# 8. 请将列表所有的元素反转，并输出反转后的列表
print('第8题：')
li = ['alex', 'eric', 'rain']
li.reverse()
print(li)

# 9. 请使用for、len、range输出列表的索引
print('第9题：')
li = ['alex', 'eric', 'rain']
for i in li:
    num = li.index(i)
    print('%s 的索引是：%d' % (li[num],num))

# 10. 请使用enumerate输出列表元素和序号（序号从100开始）
print('第10题：')
li = ['alex', 'eric', 'rain']
for index, i in enumerate(li):
    print(index + 100, i)

# 11. 请使用for循环输出列表的所有元素
print('第11题：')
li = ['alex', 'eric', 'rain']
for i in li:
    print(i, end = ' ')