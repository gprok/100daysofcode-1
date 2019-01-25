import pymysql

db = pymysql.connect("localhost","test","test","test")

cursor = db.cursor()

cursor.execute("SELECT * FROM demo")

results = cursor.fetchall()

for row in results:
    name = row[1]
    print(name)
