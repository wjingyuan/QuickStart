# 请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li = ['alex', 'eric', 'rain']

li = ['alex', 'eric', 'rain']
li.insert(li.index('eric'), '_')
li.insert(li.index('rain'), '_')
string = ''
for i in range(len(li)):
    string += li[i]
print(string)

a = '_'
i = a.join(li) # 将a插入到li中间进行分隔，但是为何是插入3个下划线？
print(i)