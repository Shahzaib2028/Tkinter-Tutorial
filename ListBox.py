from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('500x500')

def add():
    global i
    l.insert(END , str(i) +" " +  a.get())
    i = i + 1
i = 1



a = Entry(window)
a.pack()
l = Listbox(window , bg = "light blue" , font = "Times 10 bold")
l.pack()

b = Button(window , text = "add item" , command = add).pack()

window.mainloop()