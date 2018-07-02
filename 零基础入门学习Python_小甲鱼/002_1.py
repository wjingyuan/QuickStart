# 编写程序：calc.py要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”

num = eval(input('请输入1~100之间的数字：'))
if isinstance(num, int):
    if 1 <= int(num) <= 100:
        print('你妹好漂亮！')
    else:
        print('你大爷好丑！')
elif isinstance(num, float):
    if 1.0 <= float(num) <= 100.0:
        print('你妹')
    else:
        print('我靠')
else:
    print('你大爷！')