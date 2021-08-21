from tkinter import*
from tkinter import messagebox
import sqlite3

t=Tk()
t.geometry("400x400")
s1=StringVar()

u1=Label(text="Enter Name",font=("",12))
u1.place(x=100,y=100)

u2=Entry(font=("",12),textvariable=s1)
u2.place(x=200,y=100,width=120)

def show1():
    db=sqlite3.connect('shivam.db')
    cr=db.cursor()
    cr.execute("delete from login where UNAME='"+s1.get()+"'")
    messagebox.showinfo("Title","Data Delete.....")
    db.commit()
    db.close()

b1=Button(text="Delete",font=("",12),command=show1)
b1.place(x=150,y=160)
t.mainloop()
