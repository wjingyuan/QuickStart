'''
给定一个年龄，然后允许用户猜3次。
如果猜对了，直接跳出循环；
如果猜错了，提示“答错了，请重新输入！”，并允许重新输入年龄；
如果猜3次都错了，输出“猜测失败”。然后询问“是否重新开始？（Y/N）”
如果用户输入Y/y，重开开始；
如果用户输入N/n，则退出循环。
'''

i = 1
real_age = 28
while i <= 3:
    age = eval(input('请输入年龄：'))
    if age == real_age:
        print('恭喜您答对了！')
        break
    else:
        if i <= 2:
            print('答错了，请重新输入！')
            i += 1
            continue
        else:
            print('猜测失败！')

    if i == 3:
        choice = input('是否重新开始？（Y/N）')
        if choice == 'Y' or choice == 'y':
            i = 1
        else:
            break


