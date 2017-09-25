from tkinter import *
root = Tk()

canvas = Canvas(width = 600,height = 600,bg = 'yellow')


x0=50
y0=50
x1=100
y1=100







for i in range(20):
	canvas.create_oval()
	canvas.create_oval()
	canvas.create_rectangle(x0-5,y0-5,x1+5,y1+5)
	x0-=5
	y0-=5
	x1+=5
	y1+=5
canvas.pack()

mainloop()