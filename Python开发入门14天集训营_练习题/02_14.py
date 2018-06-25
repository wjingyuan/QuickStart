'''
写一个循环，不断地询问用户想买什么，
用户选择一个商品编号，就把对应的商品添加到购物车里，
最终用户输入q退出时，打印购物车里的商品列表。
'''

# 给定的商品列表
products = [
    ['Iphone 8', 6888],
    ['MacPro', 14800],
    ['小米6', 2499],
    ['Coffee', 31],
    ['Book', 80],
    ['Nike Shoes', 799]
]

# 先打印商品列表，便于客户根据商品编号选择需购买的商品。
print('----------商品列表----------')
for i in products:
    num = products.index(i)
    goods = products[num][0]
    price = products[num][1]
    print("%s. %s   %s" % (num, goods, price))

shopping_card = []
# 客户将商品添加到购物车的实现过程。
while True:
    # 通过input()输入的内容，其数据类型为字符串。
    # 首先，需要判断用户是否需要退出。
    # 其次，判断用户输入的编号是否超出商品列表编号。
    # 再次，如何输入合法，则将商品列表里对应的商品添加到购物车“shopping_card”。
    # 最后，如果输入的内容是其他字符，说明输入不合法，要求重新输入。
    x = input('请输入想购买的商品编号：')
    if x == 'q' or x == 'Q':
        if len(shopping_card) == 0:
            print('您的购物车是空的。')
            break
        else:
            print('---------已购买的商品---------')
            # 由于不知道客户往购物车里添加了多少商品，且商品具体是什么，因此无法打印购物车里的商品列表。
            # 如果需要打印购物车的商品列表，首先需要知道购物车的大小。
            # 通过循环，利用列表的特性，逐一检索出购物车中的商品。最后将购物车的商品列表打印。
            for y in range(len(shopping_card)):  # 通过len()可以知道购物车大小，通过range()可以获取购物车中每一件商品的编号列表。
                # 知道购物车中商品列表的编号，就可以检索出购物车中的商品。但需要注意，购物车中商品是一个列表，包含产品名和价格。
                print('%s. %s    %s' % (y, shopping_card[y][0], shopping_card[y][1]))
            break
    elif eval(x) < 0 or eval(x) > 5:
        print('输入的商品编号超出商品列表编号范围，请重新输入。')
        continue
    elif 0 <= eval(x) <= 5:
        shopping_card.append(products[eval(x)])
    else:
        print('内容输入错误，请重新输入需要购买的商品编号。')
        continue

