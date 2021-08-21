import sqlite3

db=sqlite3.connect('abhi.db')
cr=db.cursor()

cr.execute("Create table login(UNAME text,UPASS text)")
db.commit()
db.close()

print("Softwaves")
    
