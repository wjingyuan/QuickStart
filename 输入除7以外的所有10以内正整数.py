# 输入除7以外的所有10以内正整数

x = 0
while x < 10:
    x = x + 1
    if x == 7:
        continue
    else:
        print(x)