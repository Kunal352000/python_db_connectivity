from tkinter import*
import sqlite3
t=Tk()
t.geometry("400x400")

def show():
    db=sqlite3.connect('shivam.db')
    cr=db.cursor()
    cr.execute("insert into login values('"+a.get()+"','"+b.get()+"')")
    db.commit()
    db.close()
    print("Data insert")
    a.set("")
    b.set("")
    
a=StringVar()
b=StringVar()

e1=Entry(font=("",15),textvariable=a)
e1.pack()

e2=Entry(font=("",15),textvariable=b)
e2.pack()

b1=Button(text="INSERT",font=("",14),command=show)
b1.pack()
