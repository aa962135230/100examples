#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = ['1','2','3','4','5','6','7']


for i in range(len(a)//2):
	temp = a[len(a)-1-i]
	a[len(a)-1-i] = a[i]
	a[i] = temp
	
	
print(a)