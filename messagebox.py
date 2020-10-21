from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("PYTROOPS")
window.configure(background = "yellow")
window.geometry('500x500')

#showinfo
#showwarning
#showerror
#askquestion
#askokcancel

def pop():
    messagebox.showinfo("Info Box" , "Welcome to Pytroops")

def pop1():
    messagebox.showwarning("Warning Box", "Warning to open this")

def pop2():
    messagebox.showerror("Warning Box", "Error 404")

def pop3():
    a = messagebox.askquestion("Question", "Are you like Pytroops?")
    if a == 'yes':
        Label(window , text = 'Thanks for liking us !!!' , bg = "yellow").pack()
    else:
        Label(window, text='please give us a review to do better for you', bg="yellow").pack()


def pop4():
    a = messagebox.askokcancel("Question", "Do you want to continue?")
    if a == 1:
        Label(window , text = 'ok we are going to continue' , bg = "yellow").pack()
    else:
        Label(window, text='bye take care', bg="yellow").pack()



btn1 = Button(window , text = "show info" , command = pop).pack()
btn2 = Button(window , text = "show warning" , command = pop1).pack()
btn3 = Button(window , text = "show error" , command = pop2).pack()
btn4 = Button(window , text = "ask question" , command = pop3).pack()
btn5 = Button(window , text = "Ok cancel" , command = pop4).pack()

window.mainloop()
