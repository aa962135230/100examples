#!/usr/bin/python
# -*- coding: UTF-8 -*-

sum = 0

for j in range(1,21):
	a = 1
	for k in range(1,j+1):
		a *= k
	sum += a
		
print(sum)
