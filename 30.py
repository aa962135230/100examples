#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = input('请输入一个数字：')
b = len(a)
c = int(a)

if a[0] == a[4] and a[1] == a[3]:
	print('%d是一个回文数' %c)