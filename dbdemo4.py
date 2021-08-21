import sqlite3

db=sqlite3.connect('shivam.db')

x=input("Enter name:-")
y=input("Enter pass:-")
cr=db.cursor()
cr.execute("insert into login(UNAME,UPASS)VALUES('"+x+"','"+y+"')")

db.commit()
db.close()

print("Insert Data")
