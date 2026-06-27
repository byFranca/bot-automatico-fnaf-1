import pyautogui as pg
import time

pg.PAUSE = 0.5 #isso evita erro de double click

def moverMouse(coordenadas):
    whidth, heigth = pg.size()
    pg.moveTo(coordenadas[0]*whidth, coordenadas[1]*heigth)
    
print("ola")
time.sleep(2)
moverMouse((0.2838541666666667, 0.04259259259259259))
pg.mouseDown()
print("acabou")