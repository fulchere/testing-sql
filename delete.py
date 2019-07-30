import sqlite3
import mysqldb
print(mysqldb)

dbport = sqlite3.connect('mytesting')
c = dbport.cursor()
print("TABLE ENTRIES BEFORE DELETE")
for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)

#c.execute("DELETE FROM numberpairs WHERE first>=0 and first < 6")
c.execute("DELETE FROM numberpairs WHERE first >=0;")

print("TABLE ENTRIES AFTER DELETE")
for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)

dbport.commit()
dbport.close()
