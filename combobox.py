from tkinter import *
from tkinter import ttk

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')



def print(event):
    if c.get() == "Pizza":
        L1 = Label(window, text= "Select Your Size", bg="yellow")
        L1.pack()
        c1 = ttk.Combobox(window , value = size)
        c1.current(0)
        c1.pack()
    else:
        l2 = Label(window, text= c.get(), bg="yellow")
        l2.pack()


items = ["Pizza" , "Burger" , "Rice" , "Juices" , "Drinks"]
size = ["Small" , "Medium" , "Large"]

c = ttk.Combobox(window , value = items)
c.current(1)
c.bind("<<ComboboxSelected>>" , print)
c.pack()

window.mainloop()