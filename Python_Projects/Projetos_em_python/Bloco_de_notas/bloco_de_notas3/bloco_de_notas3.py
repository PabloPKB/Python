# -*- coding: utf-8 -*-

# Import libraries
from cgitb import text
import tkinter

# Crete a TKinter window
window = tkinter.Tk()


# Properties of the window

# Functions
def new_file():
    text_area.delete(1.0, 'end')


def save():
    text = text_area.get(1.0, 'end')
    file_save = open('file.txt', 'w')
    file_save.write(text)
    file_save.close()


def open_file():
    file = open('file.txt', 'r')
    file_open = file.read()
    text_area.insert(1.0, file_open)


def update_fonte():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font=f'{font} {size}')


window.title("Bloco de Notas com TKinter")
window.minsize(width=1280, height=720)
# window.geometry("1280x720")

# Toolbar
frame = tkinter.Frame(window, height=30)
frame.pack(fill='x')

font_text = tkinter.Label(frame, text='Font:')
font_text.pack(side='left')

spin_font = tkinter.Spinbox(frame, values=('Arial', 'Verdana'))
spin_font.pack(side='left')

# Area of text
text_area = tkinter.Text(window, font='Arial 15 bold', width=1280, height=720)
text_area.pack()

font_size = tkinter.Label(frame, text='font size: ')
font_size.pack(side='left')

spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side='left')

button_update = tkinter.Button(frame, text='Set', command=update_fonte)
button_update.pack(side='left')

#  Create a menu main and options

menu = tkinter.Menu(window)

file = tkinter.Menu(window, tearoff=0)
file.add_command(label="New", command=new_file)
file.add_command(label='Open', command=open_file)
file.add_command(label='Save', command=save)
file.add_command(label='Exit', command=window.quit)

menu = tkinter.Menu(window)
menu.add_cascade(labe='File', menu=file)
window.config(menu=menu)

window.mainloop()