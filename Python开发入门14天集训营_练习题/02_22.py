'''
转换：
1. 将字符串s = 'alex'转换成列表
2. 将字符串s= 'alex'转换成元祖
3. 将列表li = ['alex', 'seven']转换成元祖
4. 将元祖tu = ('Alex', 'seven')转换成列表
5. 将列表li = ['alex', 'seven']转换成字典且字典的key按照10开始向后递增
'''

print("1. 将字符串s = 'alex'转换成列表")
s_1 = 'alex'
a = list(s_1)
print(a)

print("2. 将字符串s = 'alex'转换成元祖")
s_2 = 'alex'
b = tuple(s_2)
print(b)

print("3. 将列表li = ['alex', 'seven']转换成元祖")
li_1 = ['alex', 'seven']
c = tuple(li_1)
print(c)

print("4. 将元祖tu = ('Alex', 'seven')转换成列表")
tu = ('Alex', 'seven')
d = list(tu)
print(d)

print("5. 将列表li = ['alex', 'seven']转换成字典且字典的key按照10开始向后递增")
li_2 = ['alex', 'seven']
k1 = li_2.index('alex') + 10
k2 = k1 + 1
e = {k1:li_2[0], k2:li_2[1]}
print(e)