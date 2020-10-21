import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "holyquran1",
    database = "pytroops",
)

window = Tk()
window.title("PYTROOPS")
window.geometry("200x200")
window.configure(background = "yellow")

def Insert():
    val1 = ent1.get()
    val2 = ent2.get()
    mycrsr = mydb.cursor()
    mycrsr.execute("CREATE TABLE IF NOT EXISTS Employees (ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR (30), Phone_no INT(11))")

    entry = "INSERT INTO Employees (Name, Phone_no) VALUES (%s, %s)"
    first = (val1, val2)

    mycrsr.execute(entry, first)
    mydb.commit()

ent1 = Entry()
ent1.grid(row = 0, column = 0)

ent2 = Entry()
ent2.grid(row = 1, column = 0, padx = 10, pady= 10)
btn = Button(window, text = "Enter value", command = Insert)
btn.grid(row = 2, column = 0 , padx = 10, pady= 10)





window.mainloop()