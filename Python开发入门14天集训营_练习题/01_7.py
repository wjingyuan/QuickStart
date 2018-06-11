# 循环打印1~100，第50次不打印，第60~80次，打印对应的平方。

i = 1
while i <= 100:
    if i == 50:
        i += 1
        continue
    elif 60 <= i <= 80:
        print(i*i)
    else:
        print(i)
    i += 1