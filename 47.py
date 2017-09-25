#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def exc(a,b):
	a,b=b,a
	return a,b
	
	
if __name__=='__main__':
	a=10
	b=20
	a,b = exc(a,b)
	print('a and b is %d and %d'%(a,b))