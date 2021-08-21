import sqlite3

db=sqlite3.connect('abhi.db')

cr=db.cursor()
cr.execute("insert into login(UNAME,UPASS) VALUES('shivam','321')")
db.commit()
db.close()

print("Insert Data.")
