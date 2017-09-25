#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 0
sum = 0

num1 = int(input('请输入数字：'))
num2 = int(input('请输入次方：'))

for x in range(num2):
	a = a*10 + num1
	sum += a
	
print('计算和为：', sum)