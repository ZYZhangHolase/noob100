#coding:utf-8
year = int(raw_input('year = \n'))
month = int(raw_input('month = \n'))
day = int(raw_input('day = \n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
days = months[month - 1] + day
leap = 0
if (year % 400 == 0) and (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if (leap == 1) and (month > 2): # 判断语句时，必须用双等于“==”
    ays = ays + 1
print 'it is the %dath day'  %days

