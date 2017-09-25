#!/usr/bin/python
# -*- coding: UTF-8 -*-


a = input('请输入你的数字：')
c = len(a)	#字符串长度
b = int(a)	

print(c)

for i in range(c-1,-1,-1):
	print(a[i])
