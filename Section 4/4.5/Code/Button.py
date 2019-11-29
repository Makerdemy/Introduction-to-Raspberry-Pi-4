import tkinter
 
window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

l1 = tkinter.Label(window, text="Learn, Explore, Make", font=("Arial Bold", 50)) 
l1.grid (column=0, row=0)

bt = tkinter.Button (window, text="Click Here For More")
bt.grid (column=0, row=2)

window.mainloop()