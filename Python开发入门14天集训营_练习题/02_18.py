'''
写代码，有如下列表，请按照功能要求实现每一个功能
li = ['hello', 'seven', ['mon', ['h', 'kelly'], 'all'], 123, 446]
1. 请根据索引输出“Kelly”
2. 请使用索引找到“all”元素，并将其修改为“ALL”，如：li[0][1][9]
'''

li = ['hello', 'seven', ['mon', ['h', 'kelly'], 'all'], 123, 446]
i = li[2][1][1]
print(i)
li[2][2] = 'ALL'
print(li)