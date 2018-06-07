'''
体质指数（BMI）=体重（kg）÷身高（m）的平方

成人的BMI数值
过轻：低于18.5
正常：18.5-24.99
过重：25-28
肥胖：28-32
非常肥胖：高于32
'''

height = float(input("请输入身高（cm）："))/100
weight = float(input("请输入体重（kg）："))
BMI = weight / height**2
if BMI < 18.5:
    print("体重过轻！")
elif BMI >= 18.5 and BMI < 24.99:
    print("体重正常！")
elif BMI >= 24.99 and BMI < 28:
    print("体重过重！")
elif BMI >= 28 and BMI < 32:
    print("肥胖！")
elif BMI >= 32:
    print("非常肥胖！")