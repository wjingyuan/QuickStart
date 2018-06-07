'''
用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果。
'''

num = eval(input('请输入一个正整数：'))
if num >0 and type(num) == int:
    a = 0
    sum = 0
    while a < num:
        a = a + 1
        sum = sum + a
    print(sum)
else:
    print('输入格式错误，请重新输入。')