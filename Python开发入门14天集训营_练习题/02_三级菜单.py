'''
需求：
可依次选择进入各子菜单
可从任意一层往回退到上一层
可从任意一层退出程序

所需新知识点：列表、字典
'''

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

current_layer = menu
layers = []
while True:
    for i in current_layer:
        print(i)
    choice = input('请输入:').strip()  # strip的作用是用于删除输入中的换行和空格
    if not choice:
        continue  # 没有输入时跳过本次循环，要求用户重新输入
    elif choice in current_layer:
        layers.append(current_layer)  # 将当前层作为一个元素保存起来，可以用列表作为容器。
        current_layer = current_layer[choice] # 让current_layer每次循环都增加一个[choice]，即：进入下一层
    elif choice == 'b' or choice == 'B':
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print('当前层为顶层！')
    elif choice == 'q' or choice == 'Q':
        print('退出菜单。')
        break
    else:
        print('输入错误,请重新输入！')