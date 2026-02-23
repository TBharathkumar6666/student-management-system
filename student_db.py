import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  
    database="student_db"
)

cursor = con.cursor()

while True:
    print("\n1.Add Student\n2.View Students\n3.Delete Student\n4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter student name: ")
        cursor.execute("insert into students(name) values(%s)", (name,))
        con.commit()
        print("Student added")

    elif ch == "2":
        cursor.execute("select * from students")
        for row in cursor.fetchall():
            print(row)

    elif ch == "3":
        sid = input("Enter student id: ")
        cursor.execute("delete from students where id=%s", (sid,))
        con.commit()
        print("Deleted")

    elif ch == "4":
        break
