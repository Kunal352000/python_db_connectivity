from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sqlite3
t=Tk()
t.geometry("600x400")
t.resizable(0,0)
f55=None
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
    showallData(n)
    searchData(n)
    updateData(n)
    deleteData(n)
    logoutData(n)
    

def insertdata(n):
    f4=Frame(bg="#091e42")
    n.add(f4,text="Insert")

    s1=StringVar()
    s2=StringVar()
    s3=StringVar()
    s4=StringVar()
    s5=StringVar()

    u1=Label(f4,font=("",11),text="Enter R.NO",bg="#091e42",fg="white")
    u1.place(x=200,y=50)
    e1=Entry(f4,font=("",11),textvariable=s1)
    e1.place(x=300,y=50,width=130)

    u2=Label(f4,font=("",11),text="Enter Name",bg="#091e42",fg="white")
    u2.place(x=200,y=100)
    e2=Entry(f4,font=("",11),textvariable=s2)
    e2.place(x=300,y=100,width=130)

    u3=Label(f4,font=("",11),text="Enter python",bg="#091e42",fg="white")
    u3.place(x=200,y=150)
    e3=Entry(f4,font=("",11),textvariable=s3)
    e3.place(x=300,y=150,width=130)

    u4=Label(f4,font=("",11),text="Enter DS&A",bg="#091e42",fg="white")
    u4.place(x=200,y=200)
    e4=Entry(f4,font=("",11),textvariable=s4)
    e4.place(x=300,y=200,width=130)

    u5=Label(f4,font=("",11),text="Enter c++",bg="#091e42",fg="white")
    u5.place(x=200,y=250)
    e5=Entry(f4,font=("",11),textvariable=s5)
    e5.place(x=300,y=250,width=130)

    def insertdemo1():
        db=sqlite3.connect('python.db')
        cr=db.cursor()
        cr.execute("insert into ins values('"+s1.get()+"','"+s2.get()+"','"+s3.get()+"','"+s4.get()+"','"+s5.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo('Title','Insert Data')
        s1.set("")
        s2.set("")
        s3.set("")
        s4.set("")
        s5.set("")
        showalldata1(f55)

    b1=Button(text="Insert",command=insertdemo1)
    b1.place(x=260,y=330,width=80,height=40)

    

def showallData(n):
    f5=Frame(bg="#091e42")
    n.add(f5,text="showAll")
    global f55
    f55=f5
    showalldata1(f5)

def showalldata1(f5):
    u1=Label(f5,text="R.NO",font=("",11),bg="#091e42",fg="white")
    u1.place(x=0,y=0,width=120)

    u2=Label(f5,text="Name",font=("",11),bg="#091e42",fg="white")
    u2.place(x=120,y=0,width=120)

    
    u3=Label(f5,text="python",font=("",11),bg="#091e42",fg="white")
    u3.place(x=240,y=0,width=120)

    
    u4=Label(f5,text="DS&A",font=("",11),bg="#091e42",fg="white")
    u4.place(x=360,y=0,width=120)

    
    u5=Label(f5,text="c++",font=("",11),bg="#091e42",fg="white")
    u5.place(x=480,y=0,width=120)

    db=sqlite3.connect('python.db')
    cr=db.cursor()
    r=cr.execute("select * from ins")
    x=0
    y=60
    for r1 in r:
        Label(f5,text=r1[0],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
        x+=120
        Label(f5,text=r1[1],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
        x+=120
        Label(f5,text=r1[2],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
        x+=120
        Label(f5,text=r1[3],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
        x+=120
        Label(f5,text=r1[4],font=("",11),bg="#091e42",fg="white").place(x=x,y=y,width=120)
        y+=40
        x=0
    db.commit()
    db.close()
def searchData(n):
    f6=Frame(bg="#091e42")
    n.add(f6,text="Search")
    s1=StringVar()

    u1=Label(f6,font=("",11),text="Enter R.NO",bg="#091e42",fg="white")
    u1.place(x=100,y=50)
    e1=Entry(f6,font=("",11),textvariable=s1)
    e1.place(x=200,y=50,width=130)

    def searchdata1():
        db=sqlite3.connect('python.db')
        cr=db.cursor()
        r=cr.execute("select * from ins where URNO='"+s1.get()+"'  ")

        for r1 in r:
            u3=Label(f6,font=("",11),text="Name is",bg="#091e42",fg="white")
            u3.place(x=200,y=100)
            u4=Label(f6,font=("",11),text=r1[1],bg="#091e42",fg="white")
            u4.place(x=300,y=100)
            u5=Label(f6,font=("",11),text="Python =",bg="#091e42",fg="white")
            u5.place(x=200,y=150)
            u6=Label(f6,font=("",11),text=r1[2],bg="#091e42",fg="white")
            u6.place(x=300,y=150)
            u7=Label(f6,font=("",11),text="DS&A =",bg="#091e42",fg="white")
            u7.place(x=200,y=200)
            u8=Label(f6,font=("",11),text=r1[3],bg="#091e42",fg="white")
            u8.place(x=300,y=200)
            u9=Label(f6,font=("",11),text="c++ =",bg="#091e42",fg="white")
            u9.place(x=200,y=250)
            u10=Label(f6,font=("",11),text=r1[4],bg="#091e42",fg="white")
            u10.place(x=300,y=250)
            break
        else:
            messagebox.showinfo('Title','Invalid R.NO')
            u13=Label(f6,font=("",11),text="",bg="#091e42",fg="white")
            u13.place(x=200,y=100,width=300)
            u14=Label(f6,font=("",11),text="",bg="#091e42",fg="white")
            u14.place(x=200,y=150,width=300)
            u15=Label(f6,font=("",11),text="",bg="#091e42",fg="white")
            u15.place(x=200,y=200,width=300)
            u16=Label(f6,font=("",11),text="",bg="#091e42",fg="white")
            u16.place(x=200,y=250,width=300)
        db.commit()
        db.close()
        
    b1=Button(f6,text="Search",font=("",11),command=searchdata1)
    b1.place(x=350,y=50,height=25)
    

def updateData(n):
    f7=Frame(bg="#091e42")
    n.add(f7,text="Update")

def deleteData(n):
    f8=Frame(bg="#091e42")
    n.add(f8,text="Delete")

def logoutData(n):
    f9=Frame(bg="#091e42")
    n.add(f9,text="logOut")


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
