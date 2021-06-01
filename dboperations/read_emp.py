import mysql.connector

conn = mysql.connector.connect(host="localhost", database="mydb", user="", password="")

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

cursor.execute("select * from emp")

#row = cursor.fetchone()

rows = cursor.fetchall()
print("Total Number of records", cursor.rowcount)

for row in rows:
    print(row)

"""
while row is not None:
    print(row)
    row = cursor.fetchone()
"""

cursor.close()
conn.close()
