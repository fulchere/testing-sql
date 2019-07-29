import sqlite3
from updown import get_list

dbport = sqlite3.connect('mytesting')
c = dbport.cursor()

try:
    with dbport:
        dbport.execute('''CREATE TABLE numberpairs(first INTEGER, second INTEGER);''')
except sqlite3.OperationalError:
    print("TABLE ALREADY EXISTS")

#for i in range(999999):
#    fr,sc = i,i+1
#    c.execute(f'''INSERT INTO numberpairs VALUES({fr},{sc});''')
for item in get_list():
    fr,sc = item[1],item[2]
    c.execute(f'''INSERT INTO numberpairs VALUES({fr},{sc});''')

print("TABLE ENTRIES AFTER INSERT")
for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)


dbport.commit()
dbport.close()
