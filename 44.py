#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[1,2,3],[4,5,6],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
	for j in range(3):
		c[i][j]=x[i][j]+y[i][j]
		
for r in c:
	print(r)
	
	
print(c)