'''
输出商品列表，用户输入序号，显示用户选中的商品
商品li = ['手机', '电脑', '鼠标垫', '游艇']
1. 允许用户添加商品
2. 用户输入序号显示内容
'''

li = ['手机', '电脑', '鼠标垫', '游艇']
shopping_card = []
print(li)
while True:
    num = input('请输入购买的商品的序号：')
    if num == 'q' or num == 'Q':
        e = input('是否退出（Y/N）：')
        if e == 'y' or e == 'Y':
            if len(shopping_card) != 0:
                print('已采购的商品：%s' % shopping_card)
                break
            else:
                print('购物车是空的。')
                break
    elif 0 <= int(num) <= len(li):
        shopping_card.append(li[int(num)])
    else:
        print('输入错误，请重新输入。')
