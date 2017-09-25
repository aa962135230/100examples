#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import *
root =Tk()

x=360
y=160
top=130
buttom = 130


canvas =Canvas(width = 400,height = 600,bg = 'white')
for i in range(20):
	canvas.create_oval(250-top,250-buttom,250+top,250+buttom)
	top -=5
	buttom += 5
canvas.pack()
mainloop()