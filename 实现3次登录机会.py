# 实现3次登录机会

n = 3
while n > 0:
    name = input("请输入账户名：")
    pwd = input("请输入密码：")
    if name == "user" and pwd == "123":
        print("登录成功！")
        break
    else:
        print("账户名或者密码错误！")
        n = n - 1