#!/usr/bin/python
# -*- coding: UTF-8 -*-

l = []
for i in range(10):
	a = int(input('请输入你的数字：'))
	l.append(a)
print(l)

for i in range(9):
    for j in range(i+1,10):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
			
print(l)