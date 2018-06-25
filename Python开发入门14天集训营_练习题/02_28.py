'''
利用For循环和range输出
1. For循环从大到小输出1-100
2. For循环从小到大输出100-1
3. While循环从大到小输出1-100
4. While循环从小到大输出100-1
'''

print('1. For循环从大到小输出1-100')
for i in range(100, 0, -1):
    print(i)

print('2. For循环从小到大输出100-1')
for i in range(1, 101):
    print(i)

print('3. While循环从大到小输出1-100')
i = 1
while i <= 100:
    print(i)
    i += 1

print('4. While循环从小到大输出100-1')
i = 100
while i >= 1:
    print(i)
    i -= 1