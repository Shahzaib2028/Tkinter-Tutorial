
from tkinter import *
from tkcalendar import *

window =  Tk()
window.geometry('500x500')
window.configure(background = "black")

l1 = Label(window, text="Select Date ", font="Times 15 bold", bg='black', fg='white')
l1.grid(row = 0 , column = 0 , pady = 10)
cal = DateEntry(window , width = 20 , background = 'blue' , borderwidth = 5 , font= 'Times 15')
cal.grid(row =  0 , column = 1 , pady = 10)

def press():
   global a
   a = cal.get_date()
   l2 = Label(window, text= "First Date", font="Times 15 bold", bg='black', fg='white')
   l2.grid(row=2, column=0)
   l3 = Label(window , text = a, font = "Times 15 bold" , bg = 'black' , fg = 'white')
   l3.grid(row = 2 , column = 1)

def press2():
   global b
   b = cal.get_date()
   l4 = Label(window, text= "Second Date", font="Times 15 bold", bg='black', fg='white')
   l4.grid(row=3, column=0)
   l5 = Label(window , text = b, font = "Times 15 bold" , bg = 'black' , fg = 'white')
   l5.grid(row = 3 , column = 1)

def diff():
    delta = a - b
    l6 = Label(window, text= "Difference", font="Times 15 bold", bg='black', fg='white')
    l6.grid(row=4, column=0)
    l7 = Label(window, text= delta.days, font="Times 15 bold", bg='black', fg='white')
    l7.grid(row=4, column=1)



btn1 = Button(window , text = "first date" , bg = "light blue" , height = 2 , width = 10  , command = press)
btn1.grid(row = 1 , column = 0)

btn2 = Button(window , text = "second date" , bg = "light blue" , height = 2 , width = 10  , command = press2)
btn2.grid(row = 1 , column = 1)

btn3 = Button(window , text = "difference" , bg = "light blue" , height = 2 , width = 10  , command = diff)
btn3.grid(row = 1 , column = 3)


window.mainloop()

