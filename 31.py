#!/usr/bin/python
# -*- coding: UTF-8 -*-

weeklist = {'M': 'Monday','T': {'u': 'Tuesday','h':'Thursday'}, 'W': 'Wednesday', 'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
letter1 = input('请输入第一个字母：')
letter1 = letter1.upper()

if (letter1 in ['T','S']):
	letter2 = input('请输入第二个字母：')
	print(weeklist[letter1][letter2])
else:
	print(weeklist[letter1])