import pyautogui as pg
import time
from pynput import keyboard

pg.PAUSE = 0.05

pausa = 0.02
rodando = True

portaEsquerdaFechada = False
portaDireitaFechada = False

coordenadas = {
    "luzDireita": (0.95546875, 0.6402777777777777),
    "luzEsquerda": (0.046875, 0.6361111111111111),
    "portaDireita": (0.9453125, 0.48194444444444445),
    "portaEsquerda": (0.04453125, 0.4625),
    "cameraAcao": (0.43072916666666666, 0.98),
    "cameraReset": (0.43072916666666666, 0.85),
    "cameraFreddy": (0.84609375, 0.8944444444444445),
    "bonnieCheckPorta": (0.12604166666666666, 0.3574074074074074),
    "chicaCheckPorta": (0.6697916666666667, 0.5333333333333333)
}

def moverMouse(posicao):
    width, height = pg.size()
    pg.moveTo(posicao[0] * width, posicao[1] * height)

def clicar(posicao):
    moverMouse(posicao)
    pg.mouseDown()
    time.sleep(pausa)
    pg.mouseUp()

def alternarCamera():
    moverMouse(coordenadas["cameraAcao"])
    time.sleep(0.1)
    moverMouse(coordenadas["cameraReset"])

def clicarCamera(nomeCamera):
    clicar(coordenadas[nomeCamera])

def abrirFecharCameraRapido():
    alternarCamera()
    time.sleep(0.3)
    alternarCamera()

def apertarBotao(nomeBotao):
    clicar(coordenadas[nomeBotao])

def checarLuzEsquerda():
    apertarBotao("luzEsquerda")
    time.sleep(0.15)
    apertarBotao("luzEsquerda")

def checarLuzDireita():
    apertarBotao("luzDireita")
    time.sleep(0.15)
    apertarBotao("luzDireita")

def alternarPortaEsquerda():
    apertarBotao("portaEsquerda")


def alternarPortaDireita():
    apertarBotao("portaDireita")

def pegarCor(posicao):
    foto = pg.screenshot()
    width, height = foto.size
    x = int(posicao[0] * width)
    y = int(posicao[1] * height)
    cor = foto.getpixel((x, y))
    return cor

def corParecida(corAtual, corEsperada, tolerancia):
    return (
        abs(corAtual[0] - corEsperada[0]) <= tolerancia and
        abs(corAtual[1] - corEsperada[1]) <= tolerancia and
        abs(corAtual[2] - corEsperada[2]) <= tolerancia
    )

def pararBot(tecla):
    global rodando
    try:
        if tecla.char == "q":
            rodando = False
            print("Parando bot...")
            return False
    except:
        pass
escutarTecla = keyboard.Listener(on_press=pararBot)
escutarTecla.start()


# Parte de execução
time.sleep(4)
while rodando:
    checarLuzDireita()
    cor = pegarCor(coordenadas["chicaCheckPorta"])
    if corParecida(cor, (86, 95, 9), 20):
        alternarPortaDireita()
        rodando = False