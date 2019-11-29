import tkinter
 
window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

rad1 = tkinter.Radiobutton(window, text='Python', value=1)
rad2 = tkinter.Radiobutton(window, text='JavaScript', value=2)
rad3 = tkinter.Radiobutton(window, text='C++', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

window.mainloop()
