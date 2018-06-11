'''
基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
'''

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