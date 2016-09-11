#coding:utf-8
def fib1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib1(n-1) + fib1(n-2)

print fib1(10)
################################################
def fib2(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print fib2(10)
################################################
def fib3(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    fibs = [0,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print fib3(10)