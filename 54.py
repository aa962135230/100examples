#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__=='__main__':
	a =input('please input your number:')
	b = len(a)
	c= []
	for i in range(-b+2,-b+6,1):
		c.append(a[i])
		
		print(a[i])
	
	print(c)