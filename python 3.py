#coding:utf-8
import math
for i in range(10000):
    x = int(math.sqrt(i+100)) #int()函数，直接截去小数部分
    y = int(math.sqrt(i+268))
    if (100 + i == x*x) and (268 + i == y*y):
        print i
