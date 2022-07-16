from PIL import Image
import pyautogui as pg
import time

im = pg.screenshot('my_screenshot.png', region=(800, 550, 350, 200))
obj = im.load()