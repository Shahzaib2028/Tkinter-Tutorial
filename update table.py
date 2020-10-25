import mysql.connector
from tkinter import *
from tkinter import ttk


data = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = 'holyquran1',
    database = 'test',
)
window = Tk()
window.title("PYTROOPS")
window.geometry("400x400")
window.configure(background = "yellow")


def Update():
    get_c1 = c1.get()
    get_c2 = c2.get()
    get_ent1 = ent1.get()
    get_ent2 = ent2.get()

    mycrsr = data.cursor()
    update = "UPDATE eployees SET %s = '%s' WHERE %s = '%s'"% (get_c1 , get_ent1 , get_c2 , get_ent2)
    mycrsr.execute(update)
    data.commit()






#mycrsr = data.cursor()

#update = "UPDATE eployees SET Phone_no = 222222 WHERE Name = 'Ali'"

#mycrsr.execute(update)
#data.commit()

val = ['Name' , "Phone_no"]
c1 = ttk.Combobox(window, value = val)
c1.grid(row = 0, column = 0)

c2 = ttk.Combobox(window, value = val)
c2.grid(row = 1, column = 0)

ent1 = Entry(window)
ent1.grid(row = 0 , column = 1, padx= 10, pady =  10)

ent2 = Entry(window)
ent2.grid(row = 1 , column = 1, padx= 10, pady =  10)

btn = Button(window , text = "UPDATE" , command = Update)
btn.grid(row = 2 , column = 0)

window.mainloop()




