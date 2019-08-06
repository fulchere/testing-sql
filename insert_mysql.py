import mysql.connector
import getpass
#ps = getpass.getpass()
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("SHOW DATABASES;")
for db in cursor:
    print(db)
cursor.execute("use iocmdatabase;")

#cursor.execute("SELECT COUNT(*) FROM record, alias WHERE alias.record_id=record.id AND record.iocinstance_id=14;")
cursor.execute("SELECT COUNT(*) as num_records FROM record WHERE record.iocinstance_id=14;")
#d = dict(cursor.fetchone()).get('num_records',None)
d = cursor.fetchone()
print(type(d))
print(d)
print(type(("""AAAA bbbb CCCC dddd""")))




'''
cursor.execute("select count(*) as num_aliases from record, alias where alias.record_id=record.id;")
for item in cursor:
    print(str(item))
    print(type(item))
'''


'''
def print_fruits():
    cursor.execute("SELECT * FROM fruits;")
    for name, price, color in cursor:
        print(f"name: {name}, price: ${price}, color: {color}")

def add_fruit(name, price, color):
    cursor.execute(f"INSERT INTO fruits VALUES('{name}',{price},'{color}')")
    print_fruits()

def delete_fruit(name):
    cursor.execute(f"DELETE FROM fruits WHERE name='{name}'")
    print_fruits()
    
#print_fruits()
#add_fruit("winterberry","2","blue")
#delete_fruit('winterberry')

def create_table():
    cursor.execute("DROP TABLE IF EXISTS numbers")
    cursor.execute("CREATE TABLE IF NOT EXISTS numbers(first DOUBLE, second DOUBLE, third DOUBLE)")

def populate_table():
    number = 0
    while (number < 100000):
        fr,sc,th = number, number*number, number*number*number
        cursor.execute(f"INSERT INTO numbers VALUES({fr},{sc},{th})")
        number += 1

def print_numbers():
    cursor.execute("SELECT * FROM numbers;")
    for fr,sc,th in cursor:
        print(f"^1: {fr}, ^2: {sc}, ^3: {th}")

def delete_numbers():
    cursor.execute("DELETE FROM numbers WHERE first<6")

create_table()
populate_table()
#print_numbers()
print("^^old\ndeleting numbers\nnewvv")
#delete_numbers()
#print_numbers()
connection.commit()
connection.close()
print("done.")'''
