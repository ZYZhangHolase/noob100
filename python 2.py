#coding:utf-8
x = int(raw_input('利润：\n'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
b = 0
for i in range(0,6):
    if x > arr[i]:
        b += (x-arr[i])*rat[i]
print b