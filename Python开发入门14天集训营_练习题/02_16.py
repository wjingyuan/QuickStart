'''
查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
'''

print('第一题:')

li = ["alec", " aric", "Alex", "Tony", "rain"]
new_li = []
for i in range(len(li)):
    element = li[i].strip()
    # if (element[0] == 'a' or element[0] == 'A') and element[-1] == 'c':
    if element.startswith('a') or element.startswith('A') and element.endswith('c'):
        new_li.append(element)
print(new_li)

print('第二题：')

tu = ("alec", " aric", "Alex", "Tony", "rain")
new_tu = []
for i in range(len(tu)):
    element = tu[i].strip()
    # if (element[0] == 'a' or element[0] == 'A') and element[-1] == 'c':
    if element.startswith('a') or element.startswith('A') and element.endswith('c'):
        new_tu.append(element)
print(tuple(new_tu))

print('第三题：')

dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
new_dic = {}
for i in dic:
    element = dic[i].strip()
    # if (element[0] == 'a' or element[0] == 'A') and element[-1] == 'c':
    if element.startswith('a') or element.startswith('A') and element.endswith('c'):
        new_dic[i] = element
print(new_dic)