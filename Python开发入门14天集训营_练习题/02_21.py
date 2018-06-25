'''
dic = {'k1':'v1', 'k2':'v2', 'k3':[11, 22, 33]}
1. 请循环输出所有的key
2. 请循环输出所有的value
3. 请循环输出所有的key和value
4. 请在字典中添加一个键值对，'k4':'v4'，输出添加后的字典
5. 请在修改字典中“k1”对应的值为“alex”，输出修改后的字典
6. 请在k3对应的值中追加一个元素44，输出修改后的字典
7. 请在k3对应的值的第1个位置插入1个元素18，输出修改后的字典
'''

dic = {'k1':'v1', 'k2':'v2', 'k3':[11, 22, 33]}

print('1. 请循环输出所有的key')
for i in dic:
    print(i, end = '')
    print()

print('2. 请循环输出所有的value')
for i in dic:
    print(dic[i], end = '')
    print()

print('3. 请循环输出所有的key和value')
for i in dic:
    print(i, dic[i])

print("4. 请在字典中添加一个键值对，'k4':'v4'，输出添加后的字典")
dic['k4'] = 'v4'
print(dic)

print('5. 请在修改字典中“k1”对应的值为“alex”，输出修改后的字典')
print('原字典为：{}'.format(dic))
dic['k1'] = 'alex'
print('新字典为：{}'.format(dic))

print('6. 请在k3对应的值中追加一个元素44，输出修改后的字典')
print('原字典为：{}'.format(dic))
dic['k3'].append(44)
print('新字典为：{}'.format(dic))

print('7. 请在k3对应的值的第1个位置插入1个元素18，输出修改后的字典')
print('原字典为：{}'.format(dic))
dic['k3'].insert(0, 18)
print('新字典为：{}'.format(dic))