#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 100
sum = 0

for i in range(10):
	sum = sum + a*2
	a = a / 2

sum=sum -100 -a

print(sum)
print(a)