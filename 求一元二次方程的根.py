'''
求一元二次方程$ ax^2+bx+c=0 $的根。
$$
x1 =（-b + \sqrt{b^2-4ac}）/(2a)
x2 = (-b - \sqrt{b^2-4ac})/(2a)
$$
首先，a<>0;
其次，b^2-4ac>=0
'''

import math

a = float(input("请输入a："))
b = float(input("请输入b："))
c = float(input("请输入c："))
delta = b**2 - 4*a*c

if a == 0:
    print("请重新输入a，且a不等于0！")
else:
    if delta == 0:
        x = -b /(2*a)
        print(x)
    elif delta > 0:
        x_1 = (-b + math.sqrt(delta))/(2*a)
        x_2 = (-b - math.sqrt(delta))/(2*a)
        print(x_1)
        print(x_2)
    else:
        print("请重新输入数值！")

