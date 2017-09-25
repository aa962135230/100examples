#!/usr/bin/python
# -*- coding: UTF-8 -*-

list1 = ['one','two','three']
a = len(list1)
list2 = []

for i in range(2,-1,-1):
	list2.append(list1[i])
	
print(list2)