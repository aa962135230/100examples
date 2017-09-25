#!/usr/bin/python
# -*- coding: UTF-8 -*-

def rabbit(num):
	i = 1
	a,b = 1,1
	while i <= num:
		yield a
		i += 1
		a,b = b , a+b
		
list = [x for x in rabbit(20)]
print(list)