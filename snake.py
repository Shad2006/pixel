from tkinter import *
w =500
h = 500
s =10
win = Tk()
win.title("Snake")
win.resizable(0,0)
c = Canvas(win, width=w, height=h)
c.pack()
win.mainloop()
x =20
y =20
x_control = 0
y_control = 0
