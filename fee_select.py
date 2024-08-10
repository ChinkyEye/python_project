import sqlite3

conn = sqlite3.connect("sqllite.db")
data = conn.execute("SELECT f.fee_id,s.st_name,f.fee_amount from fee as f inner join student as s on f.st_id = s.st_id")
print("ID","Student_id","Amount","Student Name")
for n in data:
    print(n[0], " ", n[1], " ", n[2])