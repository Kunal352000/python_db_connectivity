import sqlite3

db=sqlite3.connect('shivam.db')
cr=db.cursor()
cr.execute("insert into login(UNAME,UPASS) VALUES('aaa','111')")
db.commit()
db.close()
print("Insert Data")
