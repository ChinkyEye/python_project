import sqlite3

conn = sqlite3.connect("sqllite.db")
ins = '''
        Insert into student (st_name,st_class,st_email) VALUES ('laxmi','seven','laxmi@gmail.com')
        '''
conn.execute(ins)
conn.commit()
conn.close()