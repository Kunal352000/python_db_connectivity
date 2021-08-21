from tkinter import*
from tkinter import messagebox
import sqlite3

t=Tk()
t.geometry("400x400")

s1=StringVar()
s2=StringVar()

u1=Label(text="Enter Name",font=("",12))
u1=place(x=100,y=100)
e1=Entry(font=("",12),textvariable=s1)
e1.place(x=200,y=100,width=120)

u2=Label(text="Enter Pass",font=("",12))
u2.place(x=100,y=150)
e2=Entry(font=("",12),show="*",textvariable=s2)
e2.place(x=200,y=150,width=120)

def show1():
    db=sqlite3.connect('shivam.db')
    cr=db.cursor()
    r=cr.execute("select * from login where UNAME = '"+s1.get()+"','"+s2.get()+"'")

for r1 in r:
    messagebox.showinfo("Title","Welcome")
    break
else:
    messagebox.showinfo("Title","Invalid user")
db.commit()
db.close()

b1=Button(text="LogIn",font=("",12),command=show1)
b1.place(x=150,y=200)
t.mainloop()
