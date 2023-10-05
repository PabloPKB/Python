# -*- coding:utf-8 -*-
# 2021 01 25 https://www.pycursos.com/tkinter-sqlite3/
from tkinter import *
import tkinter.messagebox
import sqlite3


class Main:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame, text="Digite sua nota: ").pack()
        self.nota = Entry(self.frame, width=35)
        self.nota.pack(fill=X, pady=5, padx=5)
        # self.separador = Frame(height=2,bd=3,relief=SUNKEN,width=100)
        # self.separador.pack()
        self.frame3 = Frame(master)
        self.frame3.pack()
        self.add = Button(self.frame3, text="Adicionar nota", command=self.adicionar)
        self.add.pack(side=LEFT)
        self.apagar = Button(self.frame3, text="Apagar nota", command=self.apagar)
        self.apagar.pack(side=LEFT)
        scrollbar = Scrollbar(master)
        scrollbar.pack(fill=Y, side=RIGHT)
        self.listbox = Listbox(master, width=50, height=20)
        self.listbox.pack(pady=5, padx=5)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # criar banco
        self.conectar = sqlite3.connect("notas.db")
        self.cursor = self.conectar.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS notas(name TEXT)")
        self.conectar.commit()
        lista = self.cursor.execute("SELECT * FROM notas")
        for i in lista:
            self.listbox.insert(END, i)

    def adicionar(self):
        notax = self.nota.get()
        if notax == "":
            tkinter.messagebox.showwarning("Error", "Insira o texto")
        else:
            self.cursor.execute("insert into notas values(?)", (notax,))
            self.conectar.commit()
            self.listbox.insert(END, notax)
            self.nota.delete(0, END)

    def apagar(self):
        notay = str(self.listbox.get(ACTIVE))[2:-3]
        print(notay)
        self.cursor.execute("DELETE FROM notas WHERE name=?", (notay,))
        self.conectar.commit()
        self.listbox.delete(ANCHOR)

    @staticmethod
    def close():
        if tkinter.messagebox.askyesno("Fechar", "Encerrar?"):
            exit()
        else:
            pass


root = Tk()
root.geometry("300x400")
root.title("Notas")
root.protocol("WM_DELETE_WINDOW", Main.close)
Main(root)
root.mainloop()
