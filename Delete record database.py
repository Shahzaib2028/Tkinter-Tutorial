import mysql.connector
from tkinter import *
from tkinter import ttk

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "holyquran1",
    database = "test",
)

window = Tk()
window.title("PYTROOPS")
window.geometry("300x300")
window.configure(background = "yellow")


def delete():
    get_c1 = c1.get()
    get_E1 = E1.get()

    cur = mydb.cursor()
    delt = "DELETE from eployees where %s='%s'"%(get_c1,get_E1)
    cur.execute(delt)
    mydb.commit()

val = ['Name' , 'Phone_no']
c1 = ttk.Combobox(window , value = val)
c1.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

E1 = Entry(window)
E1.grid(row = 0 , column = 1)
btn = Button(window, text = 'Delete' , command = delete )
btn.grid(row = 1 , column = 0, padx = 10, pady = 10)

window.mainloop()