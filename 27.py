#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = input("请输入你的5个字符：")
l = len(s)

def output(s,l):
	if l==0:
		return
	print(s[l-1])
	output(s,l-1)
		
output(s,l)
