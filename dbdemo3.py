import sqlite3

db=sqlite3.connect('shivam.db')

x='bbb'
y='222'

cr=db.cursor()

cr.execute("insert into login(UNAME,UPASS)VALUES('"+x+"','"+y+"')")

db.commit()
db.close()

print("insert data")
