import sqlite3

db=sqlite3.connect('shivam.db')

cr=db.cursor()
x=input("Enter your name =")
y=input("Enter your pass =")

r=cr.execute("select * login where UNAME '"+x+"' AND UPASS '"+y+"' ")

for r1 in r:
    print('Welcome')
    break
else:
    print("Invalid user name and password")

db.commit()
db.close()
