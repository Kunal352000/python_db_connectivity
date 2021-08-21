import sqlite3
db=sqlite3.connect('python.db')
cr=db.cursor()
cr.execute('create table regis(UNAME text,UPASS text,UCN text)')
db.commit()
db.close()
print('table create')
