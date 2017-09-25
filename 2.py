#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = int(input('请输入企业的利润：'))


if a <= 10 :
	b = a * 0.1
elif 10 < a and a <= 20:
	b = 10*0.1+(a-10)*0.075
elif 20 < a and a <= 40:
	b = 1.75+(a-20)*0.05
elif 40 < a and a <= 60:
	b = 2.75+(a-40)*0.03
elif 60 < a and a <= 100:
	b = 3.35+(a-60)*0.015
else:
	b = 3.95 + (a - 100)*0.01
	
print(b)

