#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
maximum = lambda x,y : (x>y)*x+(x<y)*y
minimum = lambda x,y : (x<y)*x+(x>y)*y

if __name__ =='__main__':
	a = 10
	b = 20
	print('the more number is %d'%maximum(a,b))
	print('the less number is %d'%minimum(a,b))