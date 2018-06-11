'''
假设分数分为5个等级，分别是A、B、C、D、E
每个等级对应的分数分别为[90,100]、[80,90)、[70,80)、[60,70)、[0,60)
本案例主要考察多分支结构的使用
'''

grade = eval(input('请输入分数：'))
if grade >= 90 and grade <= 100:
    print('成绩等级为：A')
elif grade >= 80:
    print('成绩等级为：B')
elif grade >= 70:
    print('成绩等级为：C')
elif grade >= 60:
    print('成绩等级为：D')
elif grade >= 0:
    print('成绩等级为：E')
else:
    print('输入错误。')