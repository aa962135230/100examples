#!/usr/bin/python
# -*- coding: UTF-8 -*-

def hello():
	print('hello,world')

def hello3():
	for i in range(3):
		hello()
		
if __name__ == '__main__':
	hello3()