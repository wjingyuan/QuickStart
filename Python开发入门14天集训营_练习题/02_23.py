'''
元素分类：
有如下值集合[11, 22, 33, 44, 55, 66, 77, 88, 99, 90]，
将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
即：{'k1':大于66的所有值, 'k2':小于66的所有值}
'''

ls = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
ls_1 = []
ls_2 = []
for i in range(len(ls)):
    if ls[i] >= 66:
        ls_1.append(ls[i])
    else:
        ls_2.append(ls[i])
print(ls_1)
print(ls_2)
