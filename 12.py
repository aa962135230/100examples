#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout

list = []

for x in range(101,201):
	for y in range(2,int(sqrt(x+1))):
		if x % y ==0:
			break
	else:
		list.append(x)

			
print(list)
print('总数为：%d' % len(list))