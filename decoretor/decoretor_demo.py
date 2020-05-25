# /usr/bin/evn python
# -*-coding:utf-8 -*-
# Author : XK
import time


def outer(func):
	def inner(*args,**kwargs):
		start_time = time.time()
		func(*args,**kwargs)
		end_time = time.time()
		print("运行时间：%0.2f"%(end_time-start_time))
	return inner

@outer
def func1(name):
	time.sleep(2)
	print("func1"+name)

func1("test123")