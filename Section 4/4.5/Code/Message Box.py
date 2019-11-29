import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

def clicked():
    tkinter.messagebox.showinfo('MAKERDEMY', 'LEARN EXPLORE MAKE')
 
btn = tkinter.Button(window,text='Click to reveal', command=clicked)
btn.grid (column=0, row=2)
window.mainloop()
