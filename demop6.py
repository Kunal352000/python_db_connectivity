from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.geometry("600x400")
t.resizable(0,0)
def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=600,height=400)

    g1=StringVar()
    g2=StringVar()
    un=Label(f2,text="Enter Name",bg="#091e42",fg="white",font=("",11))
    un.place(x=200,y=50)
    e1=Entry(f2,font=("",11),textvariable=g1)
    e1.place(x=300,y=50,width=130)

    up=Label(f2,text="Enter Pass",bg="#091e42",fg="white",font=("",11))
    up.place(x=200,y=100)
    e2=Entry(f2,font=("",11),show="*",textvariable=g2)
    e2.place(x=300,y=100,width=130)

    def login1():
        db=sqlite3.connect('python.db')
        cr=db.cursor()
        r=cr.execute("select * from regis where UNAME='"+g1.get()+"' AND UPASS= '"+g2.get()+"' ")
        for r1 in r:
            mymenu()
            break
        else:
            messagebox.showinfo('Title','Invalid username and password')
        db.commit()
        db.close()
        g1.set=("")
        g2.set=("")

    b1=Button(f2,text="Login",command=login1)
    b1.place(x=260,y=160,width=100,height=40)
    b2=Button(f2,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)
    b1=Button(f2,text="Regis",command=regis)
    b1.place(x=480,y=340,width=100,height=40)

def mymenu():
    n=ttk.Notebook()
    n.place(x=0,y=0,width=600,height=400)
    insertdata(n)

def insertdata(n):
    f4=Frame(bg="#091e42")
    n.add(f4,text="Insert")

def regis():
    f3=Frame(bg="#091e42")
    f3.place(x=0,y=0,width=600,height=400)

    r1=StringVar()
    r2=StringVar()
    r3=StringVar()
    
    un=Label(f3,text="Enter Name",bg="#091e42",fg="white",font=("",11))
    un.place(x=200,y=50)
    e1=Entry(f3,font=("",11),textvariable=r1)
    e1.place(x=300,y=50,width=130)

    up=Label(f3,text="Enter Pass",bg="#091e42",fg="white",font=("",11))
    up.place(x=200,y=100)
    e2=Entry(f3,font=("",11),show="*",textvariable=r2)
    e2.place(x=300,y=100,width=130)

    uc=Label(f3,text="Enter C.N",bg="#091e42",fg="white",font=("",11))
    uc.place(x=200,y=150)
    e3=Entry(f3,font=("",11),textvariable=r3)
    e3.place(x=300,y=150,width=130)

    def regis1():
        db=sqlite3.connect('python.db')
        cr=db.cursor()
        cr.execute("insert into regis values('"+r1.get()+"','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo('Title','User Register')
        r1.set("")
        r2.set("")
        r3.set("")
    
    b1=Button(f3,text="Regis",command=regis1)
    b1.place(x=260,y=210,width=100,height=40)

    b2=Button(f3,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)

    b3=Button(f3,text="Login",command=login)
    b3.place(x=480,y=340,width=100,height=40)

def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)

    b1=Button(f1,text="Login",command=login)
    b1.place(x=220,y=100,width=80,height=40)

    b2=Button(f1,text="Regis",command=regis)
    b2.place(x=310,y=100,width=80,height=40)

home()
t.mainloop()
