import sqlite3
db=sqlite3.connect('python.db')
cr=db.cursor()
cr.execute('create table ins(URNO text,UNAME text,UPHY text,UDS text,UC text)')
db.commit()
db.close()
print('Table create')
