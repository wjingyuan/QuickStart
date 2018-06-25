'''
有两个列表
l1 = [11, 22, 33]
l2 = [22, 33, 44]
1. 获取内容相同的元素列表
2. 获取l1中有,l2中没有的元素列表
3. 获取l2中有，l3中没有的元素列表
4. 获取l1和l2中内容都相同的元素
'''

l1 = [11, 22, 33]
l2 = [22, 33, 44]

print('1. 获取内容相同的元素列表')
ls_1 = []
for i in range(len(l1)):
    if l1[i] in l2:
        ls_1.append(l1[i])
print(ls_1)

print('2. 获取l1中有,l2中没有的元素列表')
ls_2 = []
for i in range(len(l1)):
    if l1[i] not in l2:
        ls_2.append(l1[i])
print(ls_2)

print('3. 获取l2中有，l1中没有的元素列表')
ls_3 = []
for i in range(len(l2)):
    if l2[i] not in l1:
        ls_3.append(l2[i])
print(ls_3)

print('4. 获取l1和l2中内容都相同的元素')
ls_3 = []
for i in range(len(l1)):
    if l1[i] in l2:
        print(l1[i])
