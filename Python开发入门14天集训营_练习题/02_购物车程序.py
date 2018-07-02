'''
基础要求：
1、启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示

扩展需求：
1、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
2、允许查询之前的消费记录
'''

# 使用termcolor库，可以高亮输出文本。使用方法为：cprint(text, color=None, on_color=None, attrs=None, **kwargs)。
# termcolor支持%s、%d格式的输出方法。
from termcolor import cprint

def buy(products, salary):
    shopping_card = []
    total_money = 0
    while True:
        x = input('请输入想购买的商品编号：')
        if x.upper() == 'Q':  # 退出时打印购物车商品
            if len(shopping_card) == 0:
                print('您的购物车是空的。')
                break
            else:
                print('---------已购买的商品---------')
                for y in range(len(shopping_card)):
                    print('%s. %s    %s' % (y, shopping_card[y]['name'], shopping_card[y]['price']))
                break
        elif int(x) < 0 or int(x) > len(products):
            print('输入的商品编号超出商品列表编号范围，请重新输入。')
            continue
        elif 0 <= int(x) <= len(products):
            # 添加商品到购物车
            shopping_card.append(products[int(x)])
            print(products[int(x)], '已成功加入购物车')
            total_money += products[int(x)]['price']
            cprint('共需支付： %d' % total_money, 'red', 'on_white', ['bold'])
            if int(salary) < total_money:
                balance = int(salary ) - total_money
                cprint('您的余额不足。当前可用余额为： %d' % balance, 'red', 'on_white', ['bold'])
                shopping_card.pop()
                continue
        else:
            print('内容输入错误，请重新输入需要购买的商品编号。')
            continue

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]

user_info = {
    'shanshan':'123',
    'Judy':'321',
    'Miller':'234',
    'Mike':'432'
}

while True:
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_info.get(user_name) == password:

        while True:
            wage = input('请输入您的月工资收入：')
            if wage.isdigit(): # 判断输入是否为数字
                break
            else:
                print('工资格式错误，请输入数字。')
                continue

        print('-----------商品列表-----------')

        for i in range(len(goods)):
            print('%s. %s  %s' % (i, goods[i]['name'], goods[i]['price']))
        buy(goods, wage)
        break

    else:
        print('用户名或密码错误，请重新输入。')
        continue