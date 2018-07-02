'''
题目：宏 #define 命令练习 (2)
#include "stdio.h"
#define exchange(a,b) { \ /* 宏定义中允许包含两道衣裳命令的情形，此时必须在最右
边加上 "\"*/
int t;\
t=a;\
a=b;\
b=t;\
}'
这个宏定义 python 不支持
'''