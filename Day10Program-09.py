import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE Cars(
      id INT,Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',35000)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
      
con.commit()
print("Values in table car inserted.")

      
