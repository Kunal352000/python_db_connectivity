import sqlite3
db=sqlite3.connect('abhi.db')

x='shivam'
y="321@"

cr=db.cursor()

cr.execute("insert into login(UNAME,UPASS) VALUES('"+x+"','"+y+"')")

db.commit()
db.close()

print("Insert Data")
