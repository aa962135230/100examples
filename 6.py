#!/usr/bin/python
# -*- coding: UTF-8 -*-


def fib(n):
	a,b = 0,1
	print(a)
	for i in range(n-1):
		a,b = b,a+b
		print(a)

fib(10)
		
