from tkinter import *

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('300x300')

def open():
    window.destroy()
    top_window = Tk()
    top_window.title('New Window')
    top_window.configure(background = "black")
    top_window.geometry('400x400')



btn = Button(window , text = 'open new window' , command = open)
btn.pack()

window.mainloop()