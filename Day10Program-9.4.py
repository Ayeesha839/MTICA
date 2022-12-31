import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute('''
UPDATE Cars
SET Name='Innova' WHERE id=4
''')
con.commit()
con.close()
print("Data Updated")
