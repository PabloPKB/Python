import pygame as pg
import pandas as pd
import random
import math

# Cores
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul_claro = (200, 200, 255)
azul = (100, 100, 255)
branco = (255, 255, 255)

# Setup da tela do Jogo
window = pg.display.set_mode((1000, 700))

# Inicializando fonte do Jogo
pg.font.init()
# Escolhendo fonte e tamanho
font = pg.font.SysFont('Courier New', 50, bold=True)

tabuleiro = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

jogo_date = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

escondendo_numeros = True
tabuleiro_preenchido = True
click_last_status = False
click_position_x = -1
click_position_y = -1
numero = 0

def Tabuleiro_Hover(window, mouse_position_x, mouse_position_y):
    quadrado = 66.7  # Pixels de tamanho
    ajuste = 50  # Pixels - direita/esquerda
    x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)
    pg.draw.rect(window, branco, (0, 0, 1000, 700))
    if x  >= 0 and x <= 8 and y >= 0 and y <= 8:  # Mapeando o tabuleiro / quadrados com a função Houver
        pg.draw.rect(window, azul_claro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

def Celula_Selecionada(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y, quadrado, ajuste):
    if click_last_status == True and click == True:  # selecionar o quadrado que será digitado o número
        x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
        y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)
        pg.draw.rect(window, azul, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()   # Fecha o jogo
        if event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)  # Identifica que tecla está sendo clicada

    # Declarando variavel da posiçãp
    mouse = pg.mouse.get_pos()  # Identificando a posição do mouse dentro do jogo
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declarando variavel do mouse
    click = pg.mouse.get_pressed()  # Indetificando o click do mouse
    # Jogo
    Tabuleiro_Hover(window, mouse_position_x, mouse_position_y)
    click_position_y = Celula_Selecionada(window, mouse_position_x, mouse_position_y, click_last_status, click[0], 
                                          click_position_x, click_position_y, quadrado=[], ajuste=[] )


    # Clucj=k Last Stauts
    if click[0] == True:
        click_last_staus = True
    else:
        click_last_staus = False

    pg.display.update()


