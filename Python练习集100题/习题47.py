'''
题目：宏 #define 命令练习 (3)
1. 程序分析：
2. 程序源代码：
#define LAG >
#define SMA <
#define EQ ==
#include "stdio.h"
void main()
{
int i=10;
int j=20;
if(i LAG j)
printf("\40: %d larger than %d \n",i,j);
else if(i EQ j)
printf("\40: %d equal to %d \n",i,j);
else if(i SMA j)
printf("\40:%d smaller than %d \n",i,j);
else
printf("\40: No such value.\n");
}
不知道如何用 python 实现类似的功能
'''