#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fun(age,rank):       #age 年龄，rank 递归第几个人
    if rank == 1:
        return age
    else:
        return fun(age+2,rank-1)
print (fun(10,5))