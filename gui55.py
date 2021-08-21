from tkinter import*
t=Tk()
t.geometry("400x400")

def show():
    print(a.get(),b.get())
a=StringVar()
b=StringVar()

e1=Entry(font=("",15),textvariable=a)
e1.pack()

e2=Entry(font=("",15),textvariable=b)
e2.pack()

b1=Button(text="INSERT",font=("",14),command=show)
b1.pack()
