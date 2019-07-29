import sqlite3

dbport = sqlite3.connect('mytesting')
c = dbport.cursor()

try:
    with dbport:
        dbport.execute('''CREATE TABLE numberpairs(first INTEGER, second INTEGER);''')
except sqlite3.OperationalError:
    print("TABLE already exists")

for i in range(1000):
    fr,sc = i,i+1
    c.execute(f'''INSERT INTO numberpairs VALUES({fr},{sc});''')

for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)

#c.execute("DELETE FROM numberpairs WHERE first>100 and second < 600")
c.execute("DELETE FROM numberpairs WHERE first>500")

for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)

dbport.commit()
dbport.close()
