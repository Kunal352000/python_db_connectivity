import sqlite3
db=sqlite3.connect('shivam.db')
cr=db.cursor()
cr.execute("update login set UPASS='ram' where UNAME='aaa'")
print("Data update")
db.commit()
db.close()
