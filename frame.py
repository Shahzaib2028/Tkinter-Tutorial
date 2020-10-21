from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.geometry("700x600")

window.configure(background = "yellow")
f1 = Frame(window , bg = "grey" , borderwidth = 8, relief = 'ridge')
f1.pack(side = LEFT , fill = "y")

f2 = Frame(window, bg = "grey" , borderwidth = 8, relief = 'ridge')
f2.pack(side = TOP , fill = "x")

f3 = Frame(window, bg = "grey" , borderwidth = 8, relief = 'ridge')
f3.pack(side = LEFT , fill = 'y')

l2 = Label(f2 , text = "PYTROOPS" ,  bg = "grey" , fg = "black" , font = "times 20 bold")
l2.pack()

l1 = Label(f1 , text = "HELLO" , bg = "grey" , fg = "black" , font = "times 20 bold")
l1.pack(pady = 250 , padx = 60)

l3 = Label(f3 , text = "SUSCRIBE" ,  bg = "grey" , fg = "black" , font = "times 20 bold")
l3.pack(padx = 155 , pady = 200)

window.mainloop()