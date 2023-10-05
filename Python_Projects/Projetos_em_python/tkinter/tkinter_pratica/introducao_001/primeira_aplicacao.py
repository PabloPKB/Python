
from tkinter import *

menu_inicial = Tk()  # CRIANDO TELA/JANELA
menu_inicial.title('App com tkinter')  # TITULO

''' Dimensão, posicionamento e redirecionamento de formulários. '''
menu_inicial.geometry("400x300+200+200")
''' 400x300 -> largura e altura da janela
200+200 -> será onde na tela ela irá abrir(coordenadas) 
'''
menu_inicial.resizable(True, True)  # ATIVANDO TAMANHO MÁXIMO E TAMANHO MÍNIMO DO APP
''' para desativar opção de maximizar app - altura/largura, so colocar False
no lugar do True
menu_inicial.resizable(False, False)
'''

menu_inicial.minsize(width=300, height=200)  # ALTURA E LARGURA - MIN DA JANELA
menu_inicial.maxsize(500, 400)  # ALTURA E LARGURA - MAX DA JANELA
''' menu_inicial.state("zoomed")  - maximiza toda a janela em toda a tela
ou- menu_inicial.state("iconic")  - minimizar toda a janela
'''



menu_inicial.mainloop()  # PARA ENCERRAR O APP