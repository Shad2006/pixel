from tkinter import *

w = 1000
h = 1000
s = 10

win = Tk()
win.title("Snake")
win.resizable(0, 0)
c = Canvas(win, width=w, height=h)
c.pack()

x = 20
y = 20
x_control = 0
y_control = 0

def snake_item(canvas, x, y):
    canvas.create_rectangle(x * s, y * s, (x + 1) * s, (y + 1) * s, fill="#000000")

def move(event):
    global x_control, y_control, x, y

    if event.keysym == "Left":
        x_control = -1
        y_control = 0
    elif event.keysym == "Right":
        x_control = 1
        y_control = 0
    elif event.keysym == "Up":
        y_control = -1
        x_control = 0
    elif event.keysym == "Down":
        y_control = 1
        x_control = 0

def game_loop():
    global x, y
    x += x_control
    y += y_control
    c.delete("all")  
    snake_item(c, x, y)
    win.after(100, game_loop)  
c.bind_all("<KeyPress-Left>", move)
c.bind_all("<KeyPress-Right>", move)
c.bind_all("<KeyPress-Up>", move)
c.bind_all("<KeyPress-Down>", move)

game_loop()  
win.mainloop()
