import pyautogui as pg
import time
from pynput import keyboard

def pegarCoordenadas(tecla):
    try:
        if tecla.char == "m":
            x, y = pg.position()
            width, height = pg.size()

            posicaoX = x / width
            posicaoY = y / height

            print(posicaoX, posicaoY)
    except:
        pass

escutarTecla = keyboard.Listener(on_press=pegarCoordenadas)
escutarTecla.start()
escutarTecla.join()

##digite ctrl + c para parar a execução do programa