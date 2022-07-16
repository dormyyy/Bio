from tkinter import *
speed = 100
tick = 0


def start():
    start_button.destroy()
    go()


def end():
    global speed, q
    ss.after(100, restart1)


def restart1():
    restart_button.place(x=280, y=130, width=40, height=40)
    player1.place(x=0, y=120, width=10, height=50)
    player2.place(x=590, y=120, width=10, height=50)
    ball.place(x=300, y=150, width=10, height=10)


def restart2():
    global q, w, x1, y1, tick
    global r1, r2, speed, score1, score2
    restart_button.place(x=600, y=300, width=40, height=40)
    l1['bg'] = '#4EDE65'
    l2['bg'] = '#78F561'
    score2_label['bg'] = '#78F561'
    score1_label['bg'] = '#4EDE65'
    tick = 0
    r1 = 120
    r2 = 120
    q = 300
    w = 150
    x1 = 10
    y1 = 10
    go()


def move1(ev1):
    global r1, q
    if q < 300 and (r1 > 0 or r1 < 600):
        if ev1.keysym == 'w' and r1 > 0:
            r1 -= 10
        elif ev1.keysym == 's' and r1 < 250:
            r1 += 10
    player1.place(x=0, y=r1, width=10, height=50)


def move2(ev1):
    global r2, q
    if q > 300:
        if ev1.keysym == 'Up' and r2 > 0:
            r2 -= 10
        elif ev1.keysym == 'Down' and r2 < 250:
            r2 += 10
    player2.place(x=590, y=r2, width=10, height=50)


def go():
    global q, w, x1, y1, tick
    global r1, r2, speed, score1, score2
    q += x1
    w += y1
    if w > 285:
        y1 = -10
    if w < 10:
        y1 = 10
    if q in range(580, 600) and w in range(r2, r2 + 51):
        x1 = -10
    if q in range(0, 20) and w in range(r1, r1 + 51):
        x1 = 10
    if q <= 300:
        l1['bg'] = '#78F561'
        l2['bg'] = '#4EDE65'
        score2_label['bg'] = '#4EDE65'
        score1_label['bg'] = '#78F561'
    else:
        l1['bg'] = '#4EDE65'
        l2['bg'] = '#78F561'
        score2_label['bg'] = '#78F561'
        score1_label['bg'] = '#4EDE65'
    ball.place(x=q, y=w, width=10, height=10)
    if q in range(0, 600):
        if tick < 90:
            tick += 1 / 5
        ss.after(int(speed - tick), go)
    else:
        if q < 300:
            score2 += 1
            l1['bg'] = '#DB2E22'
            score1_label['bg'] = '#DB2E22'
            score2_label['text'] = score2
        else:
            l2['bg'] = '#DB2E22'
            score1 += 1
            score2_label['bg'] = '#DB2E22'
            score1_label['text'] = score1
        end()


ss = Tk()
ss.geometry('600x300')
ss.resizable(False, False)
l1 = Label(ss, bg='#4EDE65')
l1.place(x=0, y=0, width=300, height=300)
l2 = Label(ss, bg='#78F561')
l2.place(x=300, y=0, width=300, height=300)
score1 = 0
score2 = 0
score2_label = Label(ss, bg='#78F561', fg='white', text='0', font=('Arial', 26))
score2_label.place(x=440, y=120)
score1_label = Label(ss, bg='#4EDE65', fg='white', text='0', font=('Arial', 26))
score1_label.place(x=140, y=120)

r1 = 120
player1 = Button(ss, bg='#fff000')
player1.place(x=0, y=r1, width=10, height=50)
player1.bind_all('<KeyPress-w>', move1)
player1.bind_all('<KeyPress-s>', move1)

r2 = 120
player2 = Button(ss, bg='#000FFF')
player2.place(x=590, y=r2, width=10, height=50)
player2.bind_all('<KeyPress-Up>', move2)
player2.bind_all('<KeyPress-Down>', move2)

q = 300
w = 150
x1 = 10
y1 = 10
ball = Button(ss, bg='red')
ball.place(x=q, y=w, width=10, height=10)
start_button = Button(ss, bg='green', text='Start', command=start)
start_button.place(x=280, y=130, width=40, height=40)
restart_button = Button(ss, text='restart', bg='green', command=restart2)

ss.mainloop()
