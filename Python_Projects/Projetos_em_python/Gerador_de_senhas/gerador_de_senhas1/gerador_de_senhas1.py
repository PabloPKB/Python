from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# IMPORTANDO PILLOW
from PIL import ImageTk, Image


# IMPORTANDO STRINGS
import string
import random


#  CORES ---------------------------------------------------------------------------------------------------------------
cor0 = "#444466"  # PRETO / BLACK
cor1 = "#feffff"  # BRANCA / WHITE
cor2 = "#f05a43"  # VERMELHA / RED

janela = Tk()
janela.title('')
janela.geometry('320x375')
janela.configure(bg=cor1)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# DIVIDINDO A TELA EM DOIS FRAMES --------------------------------------------------------------------------------------
#                          largura    altura                              relevo  liso
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=300, height=315, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# TRABALHANDO NO FRAME CIMA --------------------------------------------------------------------------------------------
img = Image.open('password.jpg')
img = img.resize((30,31), Image.ANTIALIAS)  # MOVIMENTAÇÃO PARA LADOS / CIMA,BAIXO
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw',
                 font='Ivy 16 bold', bg=cor1, fg=cor0)
app_nome.place(x=37, y=3)

app_linha = Label(frame_cima, text='', width=500, height=1, padx=0, relief='flat', anchor='nw', font='Ivy 1 bold',
                  bg=cor2, fg=cor0)
app_linha.place(x=0, y=45)

# FUNÇÃO GERAR SENHA ---------------------------------------------------------------------------------------------------
def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros ='0123456789'
    simbolos = '{}[]()-_=@#.;'


    global combinar

    combinar = alfa_maior + alfa_menor + numeros + simbolos

    #  CONDIÇÃO PARA MAIÚSCULAS
    if estado_1.get() == alfa_maior:
        combinar =  alfa_maior
    else:
        pass

    # CONDIÇÃO PARA MINÚSCULAS
    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

    #  CONDIÇÃO PARA NÚMEROS
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # CONDIÇÃO PARA SIMBOLOS
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass


    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Senha copiada com sucesso")

    app_botao_copiar = Button(frame_baixo,command=copiar_senha, text='COPIAR', width=6, height=2, relief='raised',
                              overrelief='solid', anchor='center', font='Ivy 10 bold', bg=cor1, fg=cor0)
    app_botao_copiar.grid(row=0, column=1, sticky=NW, padx=0, pady=15, columnspan=1)


# TRABALHAR NO FRAME DOIS ----------------------------------------------------------------------------------------------
app_senha = Label(frame_baixo, text=' * * * * * * * * * * ', width=8, height=2, padx=0, relief='solid',
                  anchor='center', font='Ivy 16 bold', bg=cor1, fg=cor0)
app_senha.grid(row=0, columnspan=1, sticky=NSEW, padx=15, pady=10)

app_info = Label(frame_baixo, text='Número total de caracteres na senha', height=1, padx=0, relief='flat',
                 anchor='center', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_info.grid(row=1, columnspan=1, sticky=NSEW, padx=5, pady=1)

var = IntVar()
var.set(10)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, columnspan=1, sticky=NW, padx=7, pady=8)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '0123456789'
simbolos = '{}[]()-_=@#.;'


frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, relief='flat')
frame_caracteres.grid(row=3, column=0,sticky=NSEW, columnspan=3)


#  LETRAS MAIUSCULAS ---------------------------------------------------------------------------------------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfa_maior, offvalue='off', relief='flat',
                      bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras maiúsculas - ABC', height=1, padx=0, relief='flat',
                 anchor='nw', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=6)


# LETRAS MINUSCULAS ----------------------------------------------------------------------------------------------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfa_menor, offvalue='off', relief='flat',
                      bg=cor1)
check_2.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Letras minúsculas - abc', height=1, padx=0, relief='flat',
                 anchor='nw', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=6)


# NÚMEROS --------------------------------------------------------------------------------------------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat',
                      bg=cor1)
check_3.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Números - 123', height=1, padx=0, relief='flat',
                 anchor='nw', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=6)


# SIMBOLOS -------------------------------------------------------------------------------------------------------------
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat',
                      bg=cor1)
check_4.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Símbolos - (@#/)', height=1, padx=0, relief='flat',
                 anchor='nw', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_info.grid(row=3, column=1, sticky=NW, padx=3, pady=6)


# BOTÃO ----------------------------------------------------------------------------------------------------------------
app_botao = Button(frame_caracteres, command=criar_senha, text='GERAR SENHA', width=38, height=2, relief='flat',
                   overrelief='solid', anchor='center', font='Ivy 10 bold', bg=cor2, fg=cor0)
app_botao.grid(row=5, column=0, sticky=NSEW, padx=3, pady=5, columnspan=5)


app_botao_copiar = Button(frame_baixo, text='COPIAR', width=6, height=2, relief='raised',overrelief='solid',
                          anchor='center', font='Ivy 10 bold', bg=cor1, fg=cor0)
app_botao_copiar.grid(row=0, column=1, sticky=NW, padx=0, pady=15, columnspan=1)

janela.mainloop()
