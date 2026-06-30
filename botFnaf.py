import pyautogui as pg
import time
from pynput import keyboard
pausa = 0.02
rodando = True

coordenadas = {
    "luzDireita": (0.95546875, 0.6402777777777777),
    "luzEsquerda": (0.046875, 0.6361111111111111),
    "portaDireita": (0.9453125, 0.48194444444444445),
    "portaEsquerda": (0.04453125, 0.4625),
    "cameraAcao": (0.43072916666666666, 0.98),
    "cameraReset": (0.43072916666666666, 0.85),
    "chicaCheckPorta" : (0.6697916666666667, 0.5333333333333333),
    "bonnieCheckSeContinuaLa1" : (0.38177083333333334, 0.40185185185185185),
    "bonnieCheckSeContinuaLa2" : (0.38229166666666664, 0.4666666666666667),
    "bonnieCheckPorta" : (0.12604166666666666, 0.3574074074074074),
    "cameraFreddy": (0.84609375, 0.8944444444444445)
}

def moverMouse(posicao):
    width, heigth = pg.size()
    pg.moveTo(posicao[0]*width, posicao[1]*heigth)
    

def clicar(posicao):
    moverMouse(posicao)
    time.sleep(0.3)
    pg.mouseDown()
    time.sleep(pausa)
    pg.mouseUp()
    
def pegarcoord():
    width, heigth = pg.size()
    mx, my = pg.position()
    posicaoX = mx/width
    posicaoY = my/heigth
    coord = posicaoX, posicaoY
    return coord
   
def pegarCor(coord):
    ft = pg.screenshot()
    width, height = ft.size
    x = int(coord[0] * width)
    y = int(coord[1] * height)
    pixel = ft.getpixel((x, y))
    return pixel 

def checarEsquerda():
    clicar(coordenadas["luzEsquerda"])
    time.sleep(0.01)
    clicar(coordenadas["luzEsquerda"])

def checarDireita():
    clicar(coordenadas["luzDireita"])
    time.sleep(0.01)
    clicar(coordenadas["luzDireita"])

def alternarCamera():
    moverMouse(coordenadas["cameraAcao"])
    time.sleep(0.1)
    moverMouse(coordenadas["cameraReset"])

def abrirFecharCameraRapido():
    alternarCamera()
    time.sleep(0.3)
    alternarCamera()

def checarFreddy():
    alternarCamera()
    time.sleep(0.3)
    clicar(coordenadas["cameraFreddy"])
    time.sleep(0.1)
    alternarCamera()

def pararBot(tecla):
    global rodando

    try:
        if tecla.char == "q":
            rodando = False
            print("Parando bot...")
    except AttributeError:
        pass

escutador = keyboard.Listener(on_press=pararBot)
escutador.start()

while rodando:
    time.sleep(0.5)
    cord = pegarcoord()
    print(pegarCor(cord))