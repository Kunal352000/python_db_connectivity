from tkinter import*
t=Tk()
t.geometry("600x400")
t.resizable(0,0)
def login():
    f2=Frame(bg="#091e42")
    f2.place(x=0,y=0,width=600,height=400)

    un=Label(f2,text="Enter Name",bg="#091e42",fg="white",font=("",11))
    un.place(x=200,y=50)
    e1=Entry(f2,font=("",11))
    e1.place(x=300,y=50,width=130)

    up=Label(f2,text="Enter Pass",bg="#091e42",fg="white",font=("",11))
    up.place(x=200,y=100)
    e2=Entry(f2,font=("",11),show="*")
    e2.place(x=300,y=100,width=130)

    b1=Button(f2,text="Login")
    b1.place(x=260,y=160,width=100,height=40)
    b2=Button(f2,text="Home",command=home)
    b2.place(x=15,y=340,width=100,height=40)
    b1=Button(f2,text="Regis")
    b1.place(x=480,y=340,width=100,height=40)

def home():
    f1=Frame(bg="#091e42")
    f1.place(x=0,y=0,width=600,height=400)

    b1=Button(f1,text="Login",command=login)
    b1.place(x=220,y=100,width=80,height=40)

    b2=Button(f1,text="Regis")
    b2.place(x=310,y=100,width=80,height=40)

home()
t.mainloop()

    
