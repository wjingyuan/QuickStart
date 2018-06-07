# 输出1~100的所有奇数

x = 0
while x < 100:
    x = x + 1
    if x % 2 == 0:
        continue
    else:
        print(x)
