# 求1-2+3-4+5-6+...+99的和
"""
1~99可以用x= 0，x=x+1求得，剩下的问题是正负号的确定。
正负号可以用(-1)^n控制，n为1~99的自然整数。
通过式子可以发现，当x为偶数时，其前面的符号为负号。
因此，当x为偶数时，n应该为奇数，可以让n和x相差1确保x为偶数时，n为奇数。
那么，让n从2开始，则(-1)^n可以确保x为偶数时，x前符号为负号。
结果为50
"""

import math

x = 0
n = 1
sum = 0
while x <= 98:
    x = x + 1
    n = n + 1
    sum = sum + x * math.pow(-1,n)
print(sum)