from tkinter import *
from tkinter import ttk

window = Tk()
window.title("CALCULATOR")
window.configure(background = "black")
ent = Entry(window , width = 30 ,  borderwidth = 10 , relief = "ridge" , font = "Times 20")
ent.grid(row = 0 , column = 0 , columnspan = 5  , pady = 10)

def button_press(num):
    curr = ent.get()
    ent.delete(0 , END)
    ent.insert(0 , str(curr) + str(num))



def equal():
    ans = ent.get()
    ent.delete(0,END)
    ent.insert(0 , eval(ans))


def clear():
    ent.delete(0 , END)

btn1 = Button(window , text = '1' , borderwidth = 5 , relief = 'ridge' , padx = 40 , pady = 20 , command = lambda : button_press(1))
btn2 = Button(window , text = '2' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(2))
btn3 = Button(window , text = '3' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20, command = lambda : button_press(3))
btn4 = Button(window , text = '4' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(4))
btn5 = Button(window , text = '5' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(5))
btn6 = Button(window , text = '6' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(6))
btn7 = Button(window , text = '7' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(7))
btn8 = Button(window , text = '8' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(8))
btn9 = Button(window , text = '9' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press(9))
btn0 = Button(window , text = '0' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20, command = lambda : button_press(0))
btn_equal = Button(window , text = '=' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = equal)
btn_clear = Button(window , text = 'C' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = clear)
btn_add = Button(window , text = '+' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20 , command = lambda : button_press("+"))
btn_sub = Button(window , text = '-' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20, command = lambda : button_press('-'))
btn_mul = Button(window , text = 'x' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20, command = lambda : button_press('*'))
btn_div = Button(window , text = '/' , borderwidth = 5 , relief = 'ridge'  , padx = 40 , pady = 20, command = lambda : button_press('/'))


btn1.grid(row = 1 , column = 0)
btn2.grid(row = 1 , column = 1)
btn3.grid(row = 1 , column = 2)
btn_add.grid(row = 1 , column = 3)
btn4.grid(row = 2 , column = 0)
btn5.grid(row = 2 , column = 1)
btn6.grid(row = 2 , column = 2)
btn_sub.grid(row = 2 , column = 3)
btn7.grid(row = 3 , column = 0)
btn8.grid(row = 3 , column = 1)
btn9.grid(row = 3 , column = 2)
btn_mul.grid(row = 3 , column = 3)
btn0.grid(row = 4 , column = 0)
btn_clear.grid(row = 4 , column = 1)
btn_equal.grid(row = 4 , column = 2)
btn_div.grid(row = 4 , column = 3)


window.mainloop()