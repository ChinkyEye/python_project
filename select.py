import sqlite3

conn = sqlite3.connect("sqllite.db")
# data = conn.execute("SELECT * from student limit 0,2")
data = conn.execute("SELECT * from student")
for n in data:
    print(n[0]," ",n[1]," ",n[2]," ",n[3])