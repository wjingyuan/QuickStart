'''
现有商品列表如下：
products = [
    ['Iphone 8', 6888],
    ['MacPro', 14800],
    ['小米6', 2499],
    ['Coffee', 31],
    ['Book', 80],
    ['Nike Shoes', 799]
]

需打印出这样的格式：
----------商品列表-----------
0. Iphone 8  6888
1. MacPro  14800
2. 小米6  2499
3. Coffee  31
4. Book  80
5. Nike Shoes  799
'''

products = [
    ['Iphone 8', 6888],
    ['MacPro', 14800],
    ['小米6', 2499],
    ['Coffee', 31],
    ['Book', 80],
    ['Nike Shoes', 799]
]

print('----------商品列表----------')
for i in products:
    num = products.index(i)
    goods = products[num][0]
    price = products[num][1]
    # print(str(num) + '.' + products[num][0] + '   ' + str(products[num][1]))
    # print(str(num) + '.', end = ' ')
    # print(goods, end = ' ')
    # print(price)
    print("%s. %s   %s" % (num, goods, price))