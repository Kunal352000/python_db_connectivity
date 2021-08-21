import sqlite3
db=sqlite3.connect('shivam.db')
cr=db.cursor()
s1=input("Enter Name = ")
s2=input("Enter pass = ")
cr.execute("update login set UPASS ='"+s2+"' where UNAME='"+s1+"'")
print("Data update")
db.commit()
db.close()
