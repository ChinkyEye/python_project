import sqlite3
conn = sqlite3.connect("sqllite.db")
conn.execute('''
    Create table Student (
    st_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    st_name VARCHAR(50),
    st_class VARCHAR(50),
    st_email VARCHAR(50)
    )
    
    Create table Fee (
    fee_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    st_id INTEGER ,
    fee_amount INTEGER

    )
    
    
''')
conn.close()