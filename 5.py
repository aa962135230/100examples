#!/usr/bin/python
# -*- coding: UTF-8 -*-

c = []

for i in range(3):
	x = int(input('x = '))
	c.append(x)
	
c.sort(reverse = True)
print(c)