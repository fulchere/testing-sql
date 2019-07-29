import sqlite3

dbport = sqlite3.connect('mytesting')
c = dbport.cursor()

try:
    with dbport:
        dbport.execute('''IF OBJECT_ID('mytesting.numberpairs','U') IS NULL BEGIN CREATE TABLE numberpairs(first text, second text); END''')
except sqlite3.OperationalError:
    print("TABLE already exists")

for i in range(9):
    fr,sc = str(i),str(i+1)
    c.execute(f'''INSERT INTO numberpairs VALUES('{fr}','{sc}');''')

for row in c.execute('''SELECT * FROM numberpairs;'''):
    print(row)

c.execute("DELETE FROM numberpairs")
print(c.fetchall())
dbport.commit()
dbport.close()
