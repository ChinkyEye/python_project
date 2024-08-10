import sqlite3

conn = sqlite3.connect("sqllite.db")
ins = '''
        Insert into fee (st_id,fee_amount) VALUES ('1',2000)
        '''
conn.execute(ins)
conn.commit()
conn.close()