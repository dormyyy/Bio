from PIL import Image
import pyautogui as pg
import time

#(211, 247, 255) небо
#(161, 116, 56) дерево
#obj[120, 90] левый пиксель
#obj[230, 90] правый пиксель
time.sleep(2)
im = pg.screenshot(region=(800, 550, 350, 200))
obj = im.load()
pg.press('left')
x = 'left'
for i in range(1000):
    im = pg.screenshot(region=(800, 550, 350, 200))
    obj = im.load()
    if x == 'left' and obj[120, 90][0] == 211:
        pg.press('left')
    elif x == 'left' and obj[120, 90][0] != 211:
        pg.press('right')
        x = 'right'
    if x == 'right' and obj[230, 90][0] == 211:
        pg.press('right')
    elif x == 'right' and obj[230, 90][0] != 211:
        pg.press('left')
        x = 'left'
