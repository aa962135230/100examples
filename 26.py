#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fun(n):
	if n==1 or n == 0:
		return 1
	else:
		return n*fun(n-1)
		
for i in range(1,6):
	print(fun(i))