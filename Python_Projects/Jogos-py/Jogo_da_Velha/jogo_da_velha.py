import tkinter
from tkinter import *
from tkinter import ttk

# Cores -----------------------------------------------------------------------
co0 = "#FFFFFF"  # branco - white
co1 = "#333333"  # preto pesado - dark black
co2 = "#fcc058"  # laranja - orange
co3 = "#38576b"  # valor - value
co4 = "#3297a8"  # azul - blue
co5 = "#fff873"  # amarelo - yellow
co6 = "#fcc058"  # laranja - orange
co7 = "#e85151"  # vermelha - red
co8 = co4  # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b"  # preto - black


# CRIANDO JANELA PRINCIPAL ----------------------------------------------------
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)


# CRIANDO JANELA EM 2 FRAMES -------------------------------------------------
frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)


# CONFIGURANDO O FRAME CIMA ---------------------------------------------------
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7 )
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text="Jogador 1", height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text="Jogador 2", height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_pontos.place(x=130, y=20)

janela.mainloop()
