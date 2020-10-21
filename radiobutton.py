from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('200x200')

take = IntVar()
take.set('1')



def func(ans):
    l1 = Label(window, text=ans)
    l1.pack()



a = Radiobutton(window , text = "Blue" ,variable = take ,  value =  1)
a.pack()
b = Radiobutton(window , text = "Green" ,variable = take,  value = 2 )
b.pack()

b1 = Button(window , text = 'click' , command = lambda : func(take.get()))
b1.pack()


window.mainloop()