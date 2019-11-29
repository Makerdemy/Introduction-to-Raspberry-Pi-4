import tkinter
 
window = tkinter.Tk()
window.title("Welcome to MAKERDEMY")

l1 = tkinter.Label(window, text="Learn, Explore, Make", font=("Arial Bold", 50)) 
l1.grid (column=0, row=0)

bt = tkinter.Button (window, text="Click Here For More")
bt.grid (column=0, row=2)

chk_state = tkinter.BooleanVar()
chk_state.set (True) #Checked by Default
chk = tkinter.Checkbutton(window, text="Keep me signed in", var=chk_state)
chk.grid(column=0, row=3)

txt = tkinter.Entry(window,width=10)
txt.grid(column=0, row=4)
def clicked():
    res = "Welcome " + txt.get()
    l1.configure(text= res)
bt2 = tkinter.Button (window, text="Click after Entering name", command=clicked)
bt2.grid (column=0, row=5)

window.mainloop()
