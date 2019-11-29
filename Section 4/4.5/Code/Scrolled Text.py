import tkinter
from tkinter import scrolledtext

window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

txt = scrolledtext.ScrolledText(window, width=40,height=10,wrap=tkinter.WORD)
txt.grid(column=0, columnspan=3)
window.mainloop()
