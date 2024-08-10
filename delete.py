import sqlite3
conn = sqlite3.connect("sqllite.db")
student_id = input("Enter the student id:")
conn.execute("DELETE FROM student where st_id = "+ student_id)
conn.commit()
conn.close()