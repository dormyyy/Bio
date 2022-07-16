from tkinter import *


def result():
    e = entry.get()
    entry.delete(0, END)
    entry.insert(0, eval(e))


def clear():
    entry.delete(0, END)


def backspace():
    e = entry.get()
    entry.delete(len(e) - 1)


def multiply():
    e = entry.get()
    entry.insert(len(e), '*')


def divide():
    e = entry.get()
    entry.insert(len(e), '/')


def minus():
    e = entry.get()
    entry.insert(len(e), '-')


def plus():
    e = entry.get()
    entry.insert(len(e), '+')


def dot():
    e = entry.get()
    entry.insert(len(e), '.')


def degree():
    e = entry.get()
    entry.insert(len(e), '**')


def right():
    e = entry.get()
    entry.insert(len(e), ')')


def left():
    e = entry.get()
    entry.insert(len(e), '(')


def one():
    e = entry.get()
    entry.insert(len(e), '1')


def two():
    e = entry.get()
    entry.insert(len(e), '2')


def three():
    e = entry.get()
    entry.insert(len(e), '3')


def four():
    e = entry.get()
    entry.insert(len(e), '4')


def five():
    e = entry.get()
    entry.insert(len(e), '5')


def six():
    e = entry.get()
    entry.insert(len(e), '6')


def seven():
    e = entry.get()
    entry.insert(len(e), '7')


def eight():
    e = entry.get()
    entry.insert(len(e), '8')


def nine():
    e = entry.get()
    entry.insert(len(e), '9')


def zero():
    e = entry.get()
    entry.insert(len(e), '0')


win = Tk()
win.geometry('400x540')
win.config(bg='black')
win.resizable(False, False)
orange = '#ff7433'

label = Label(win, text='Калькулятор', font=('Arial', 14), bg='black', fg=orange)
label.place(relx=0.01, rely=0)
entry = Entry(win, font=('Arial', 16), width=28, bg='black', fg=orange)
entry.place(relx=0.01, rely=0.06)
backspace_button = Button(win, text='←', font=('Arial', 11), width=2, height=1, command=backspace, bg=orange, fg='white')
backspace_button.place(relx=0.9, rely=0.06)

clear_button = Button(win, text='CE', font=('Arial', 16), width=5, height=2, command=clear, bg='black', fg=orange)
multiply_button = Button(win, text='*', font=('Arial', 16), width=5, height=2, command=multiply, bg='black', fg=orange)
divide_button = Button(win, text='/', font=('Arial', 16), width=5, height=2, command=divide, bg='black', fg=orange)
minus_button = Button(win, text='-', font=('Arial', 16), width=5, height=2, command=minus,
                      bg='black', fg=orange)
clear_button.place(relx=0.03, rely=0.13)
multiply_button.place(relx=0.27, rely=0.13)
divide_button.place(relx=0.51, rely=0.13)
minus_button.place(relx=0.75, rely=0.13)

seven_button = Button(win, text='7', font=('Arial', 16), width=5, height=2, command=seven, bg='black', fg='white')
four_button = Button(win, text='4', font=('Arial', 16), width=5, height=2, command=four, bg='black', fg='white')
one_button = Button(win, text='1', font=('Arial', 16), width=5, height=2, command=one, bg='black', fg='white')
zero_button = Button(win, text='0', font=('Arial', 16), width=5, height=2, command=zero, bg='black', fg='white')
seven_button.place(relx=0.03, rely=0.31)
four_button.place(relx=0.03, rely=0.49)
one_button.place(relx=0.03, rely=0.66)
zero_button.place(relx=0.03, rely=0.83)

eight_button = Button(win, text='8', font=('Arial', 16), width=5, height=2, command=eight, bg='black', fg='white')
five_button = Button(win, text='5', font=('Arial', 16), width=5, height=2, command=five, bg='black', fg='white')
two_button = Button(win, text='2', font=('Arial', 16), width=5, height=2, command=two, bg='black', fg='white')
left_button = Button(win, text='(', font=('Arial', 16), width=5, height=2, command=left, bg='black', fg=orange)
eight_button.place(relx=0.27, rely=0.31)
five_button.place(relx=0.27, rely=0.49)
two_button.place(relx=0.27, rely=0.66)
left_button.place(relx=0.27, rely=0.83)

nine_button = Button(win, text='9', font=('Arial', 16), width=5, height=2, command=nine, bg='black', fg='white')
six_button = Button(win, text='6', font=('Arial', 16), width=5, height=2, command=six, bg='black', fg='white')
three_button = Button(win, text='3', font=('Arial', 16), width=5, height=2, command=three, bg='black', fg='white')
right_button = Button(win, text=')', font=('Arial', 16), width=5, height=2, command=right, bg='black', fg=orange)
nine_button.place(relx=0.51, rely=0.31)
six_button.place(relx=0.51, rely=0.49)
three_button.place(relx=0.51, rely=0.66)
right_button.place(relx=0.51, rely=0.83)

plus_button = Button(win, text='+', font=('Arial', 16), width=5, height=2, command=plus, bg='black', fg=orange)
result_button = Button(win, text='=', font=('Arial', 16), width=5, height=2, command=result,
                       bg=orange, fg='white')
dot_button = Button(win, text='.', font=('Arial', 16), width=5, height=2, command=dot,
                    bg='black', fg='white')
degree_button = Button(win, text='^', font=('Arial', 16), width=5, height=2, command=degree, bg='black', fg=orange)
plus_button.place(relx=0.75, rely=0.31)
result_button.place(relx=0.75, rely=0.49)
dot_button.place(relx=0.75, rely=0.66)
degree_button.place(relx=0.75, rely=0.83)

win.mainloop()
