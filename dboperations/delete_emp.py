import mysql.connector


def delete(id):
    conn = mysql.connector.connect(host="localhost", database="mydb", user="", password="")

    if conn.is_connected():
        print("Connected to mysql db")

        cursor = conn.cursor()
        str = "delete from emp where emp ='%d'"
        args = id

        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee Deleted")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()


empId = int(input("Enter Emp Id: "))
delete(empId)
