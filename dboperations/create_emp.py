import mysql.connector

conn = mysql.connector.connect(host="localhost", database="mydb", user="", password="")

if conn.is_connected():
    print("Connected to mysql db")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(3, 'Tales', 810)")
    conn.commit()
    print("Employee Added")
except:
    conn.rollback()

cursor.close()
conn.close()
