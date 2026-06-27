import pyautogui as pg
import time
from pynput import keyboard


def pressionar(tecla):
    try:
        if tecla.char == "p":
            print("ola")
    except:
        print("essa nao")

listner = keyboard.Listener(on_press=pressionar)
listner.start()
while True:
    x, y = pg.position()
    width, height = pg.size()

    percent_x = x / width
    percent_y = y / height

    print(percent_x, percent_y)
    time.sleep(0.5)
    