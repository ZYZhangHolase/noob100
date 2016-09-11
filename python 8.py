#coding:utf-8
print 'exercise_8'
import time
for i in range(1,61):
	time.sleep(1)
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())