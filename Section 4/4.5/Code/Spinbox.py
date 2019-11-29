import tkinter

window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

spin = tkinter.Spinbox(window, from_=0, to=100, width=5)
spin.grid (column=0, row=2)

window.mainloop()

