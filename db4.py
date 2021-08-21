import sqlite3

db=sqlite3.connect('abhi.db')

x=input("Enter Name: ")
y=input("Enter Pass: ")

cr=db.cursor()

cr.execute("insert into Login(UNAME,UPASS) VALUES ('"+x+"','"+y+"')")

db.commit()
db.close()

print("insert Data")
