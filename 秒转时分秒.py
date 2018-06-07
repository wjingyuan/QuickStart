'''
要求：
接收用户输入的一个秒数（非负整数），折合成小时、分钟和秒输出。
输入格式：70000
输出格式：29h 26min 40s
'''

second = int(input("请输入一个秒数(如：70000）："))
if second <0 or type(second) is float:
    print("格式输入错误！")
else:
    second2 = int(second % 60) # 求时间格式转换后的秒数
    minute = second / 60 # 求剩下的总分钟数
    minute2 = int(minute % 60) # 求时间转换后的分钟数
    hour = int(minute / 60) # 求时间转换后的小时数
    print(hour,"h",minute2,"min",second2,"s")