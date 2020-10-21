from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('500x500')

s = Scrollbar(window)
s.pack(side = 'right' , fill = 'y')
l = Listbox(window , bg = "light blue" , font = "Times 10 bold"  , yscrollcommand = s.set)
l.pack(fill = 'both' , padx = 20 , pady = 20)

s.config(command = l.yview)


for i in range(500):
    l.insert(END , i)

window.mainloop()