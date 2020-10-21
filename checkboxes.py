from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')

take = StringVar()
take1 = StringVar()


a = Checkbutton(window , text = 'Pizza' , variable = take , bg = 'yellow'  , onvalue = "Pizza" ).pack()
b = Checkbutton(window , text = 'burger' , variable = take1 , bg = 'yellow' , onvalue = "Burger" ).pack()

def print():
    lst = [take.get() , take1.get()]
    l1 = Label(window , text = lst , bg = 'yellow').pack()

b1 = Button(window , text = 'show' , command = print).pack()


window.mainloop()