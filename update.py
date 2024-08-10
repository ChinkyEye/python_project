import sqlite3
conn = sqlite3.connect("sqllite.db")
student_id = input("Enter the student id:")
student_name = input("Enter the student Name:")
conn.execute("update student set st_name = '"+student_name+"'  where st_id=" + student_id)
# conn.execute("update student set st_name = ?  where st_id= ?",(student_name,student_id))
conn.commit()
conn.close()