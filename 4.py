#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(input('your year:'))
month = int(input('your month:'))
day = int(input('your day:'))

months = [0,31,59,90,120,151,181,212,243,273,304,334]

if (year%4 == 0)and(year %400!=0)and(month>=3):
	days = months[month-1]+day+1
else:
	days = months[month-1]+day

print('it is the %dth day.' % days)