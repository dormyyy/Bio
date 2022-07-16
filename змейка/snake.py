from tkinter import *
from random import randint

# vars
score = 0
w_width = 1200
w_height = 800
head_col = '#24ffc4'
body_col = '#0f1ab2'
snake_len = 3
bg_col = 'black'
space_size = 25
food_col = '#ff42d0'
speed = 150
direction = 'right'


# classes
class Snake:
    def __init__(self):
        self.snake_len = snake_len
        self.coord = [[0, 0]] * 3
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=body_col)
            self.squares.append(square)


def move(snake, food):
    for x, y in snake.coord:
        square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=body_col)
    x, y = snake.coord[0]

    if direction == 'down':
        y += space_size
    elif direction == 'up':
        y -= space_size
    elif direction == 'right':
        x += space_size
    elif direction == 'left':
        x -= space_size

    snake.coord.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=head_col)
    snake.squares.insert(0, square)

    if x == food.coord[0] and y == food.coord[1]:
        global score
        score += 1
        l_score['text'] = f'Score: {score}'
        canvas.delete('food')

        food = Food()
    else:
        x, y = snake.coord[-1]
        square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=bg_col)

        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        win.after(speed, move, snake, food)


class Food:
    def __init__(self):
        x = randint(0, (w_width // space_size) - 1) * space_size
        y = randint(0, (w_height // space_size) - 1) * space_size

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=food_col)


def change_direction(new_dir):
    global direction

    if new_dir == 'down':
        if direction != 'up':
            direction = new_dir
    elif new_dir == 'up':
        if direction != 'down':
            direction = new_dir
    elif new_dir == 'right':
        if direction != 'left':
            direction = new_dir
    elif new_dir == 'left':
        if direction != 'right':
            direction = new_dir


def check_collisions(snake):
    x, y = snake.coord[0]

    if x < 0 or x >= w_width:
        return True
    elif y < 0 or y >= w_height:
        return True

    for snake_len in snake.coord[1:]:
        if x == snake_len[0] and y == snake_len[1]:
            return True


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Futura PT', 50), text='Game Over', fill='red')
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('Futura PT', 50), text='\n\nTry again', fill='blue')


win = Tk()
win.title('Змейка')
win.resizable(False, False)
photo = PhotoImage(file='snake.png')
win.iconphoto(False, photo)
win.config(bg=bg_col)

l_score = Label(win, text=f'Score: {score}', font='Arial 25', bg=bg_col, fg='white')
l_score.pack()

canvas = Canvas(win, height=w_height, width=w_width, bg=bg_col)
canvas.pack()

win.geometry('1200x800')

win.bind('<Down>', lambda event: change_direction('down'))
win.bind('<Up>', lambda event: change_direction('up'))
win.bind('<Right>', lambda event: change_direction('right'))
win.bind('<Left>', lambda event: change_direction('left'))

snake = Snake()
food = Food()

move(snake, food)

win.mainloop()
