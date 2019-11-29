import tkinter
 
window = tkinter.Tk()
window.title("Python GUI")

 
l1 = tkinter.Label(window, text="edureka!", font=("Arial Bold", 50))
 
l1.grid (column=0, row=0)

window.mainloop()