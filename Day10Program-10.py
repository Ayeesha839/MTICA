import sqlite3
carData=[
    (1,'Audi',100000),
    (2,'BMW',542567),
    (3,'Benz',2478786),
    (4,'Fortuner',656753)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(id INT,Name TEXT,Price INT)")
cur.executemany("INSERT  INTO Cars VALUES(?, ?, ?)",carData)
con.commit()
con.close()
print("Values inserted.")
