from tkinter import *
from random import randint
ss = Tk()
ss.geometry('600x400')

w = 200
h = [0, 0, 0]
for i in range(3):
    h[i] = randint(10, 350)
r = [250, 500, 750]
b = Button(ss, bg='#fff000')
b.place(x=150, y=w, width=20, height=20)
b11 = Button(ss, bg='#000fff')
b12 = Button(ss, bg='#000fff')
b11.place(x=r[0], y=0, width=40, height=h[0])
b12.place(x=r[0], y=h[0] + 100, width=40, height=300 - h[0])

b21 = Button(ss, bg='#000fff')
b22 = Button(ss, bg='#000fff')
b21.place(x=r[1], y=0, width=40, height=h[1])
b22.place(x=r[1], y=h[1] + 100, width=40, height=300 - h[1])

b31 = Button(ss, bg='#000fff')
b32 = Button(ss, bg='#000fff')
b31.place(x=r[2], y=0, width=40, height=h[2])
b32.place(x=r[2], y=h[2] + 100, width=40, height=300 - h[2])

s = 0
l = Label(ss, text=s, font=('Arial', 24))
l.place(x=550, y=10)


def trip():
    global w, r, s, l
    w += 1
    r[0] -= 1
    r[1] -= 1
    r[2] -= 1
    b.place(x=150, y=w, width=20, height=20)

    b11.place(x=r[0], y=0, width=40, height=h[0])
    b12.place(x=r[0], y=h[0] + 100, width=40, height=300 - h[0])

    b21.place(x=r[1], y=0, width=40, height=h[1])
    b22.place(x=r[1], y=h[1] + 100, width=40, height=300 - h[1])

    b31.place(x=r[2], y=0, width=40, height=h[2])
    b32.place(x=r[2], y=h[2] + 100, width=40, height=300 - h[2])
    if r[0] == -40:
        r[0] = 710
    if r[1] == -40:
        r[1] = 710
    if r[2] == -40:
        r[2] = 710
    if r[0] == 150 and (w < h[0] or w > h[0] + 100):
        if w < h[0] or w > 300 - h[0]:
            ss1 = Tk()
            l = Label(ss1, text='GAME OVER', font=('Arial', 20))
            l.pack()
            ss.destroy()
    elif r[1] == 150 and (w < h[1] or w > h[1] + 100):
        if w < h[1] or w > 300 - h[1]:
            ss1 = Tk()
            l = Label(ss1, text='GAME OVER', font=('Arial', 20))
            l.pack()
            ss.destroy()
    elif r[2] == 150 and (w < h[2] or w > h[2] + 100):
        if w < h[2] or w > 300 - h[2]:
            ss1 = Tk()
            l = Label(ss1, text='GAME OVER', font=('Arial', 20))
            l.pack()
            ss.destroy()
    elif r[0] == 150 and (w > h[0] or w < h[0] + 100):
        s += 1
        l['text'] = str(s)
    elif r[1] == 150 and (w > h[1] or w < h[1] + 100):
        s += 1
        l['text'] = str(s)
    elif r[2] == 150 and (w > h[2] or w < h[2] + 100):
        s += 1
        l['text'] = str(s)
    ss.after(10, trip)


def move(s):
    global w
    if s.keysym == 'space':
        w -= 30
        b.place(x=150, y=w, width=20, height=20)


b.bind_all('<KeyPress-space>', move)

trip()
ss.mainloop()
