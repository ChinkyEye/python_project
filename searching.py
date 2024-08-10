import sqlite3

conn = sqlite3.connect("sqllite.db")
# data = conn.execute("SELECT * from student limit 0,2")
data = conn.execute("SELECT * from student")
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])

print()

student_name = input("Enter the name:")
# data = conn.execute("SELECT * FROM student where st_name='"+student_name+"'")
data = conn.execute("SELECT * FROM student where st_name like '%"+student_name+"%'")
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])