'''
打印九九乘法表
待解决问题：
1. 如何删除m分别为1、2、3……时每一行最后一个逗号？
2. 如何排版，让九九乘法表更好看？
'''

for m in range(1,10):
    for n in range(1,10):
        print('{}*{}={}'.format(m,n,m*n),end = ',')
    print(end = '\n')