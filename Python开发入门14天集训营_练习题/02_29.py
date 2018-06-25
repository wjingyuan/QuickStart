'''
利用for循环和range输出9*9乘法表
'''

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = %d' % (j, i, i*j), end = ' ')
        if i == j:
            break
    print()