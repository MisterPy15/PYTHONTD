import sqlite3

def create_db():

    conn = sqlite3.connect(database="To_DoList.db")
    cur = conn.cursor()
    
    query = "CREATE TABLE IF NOT EXISTS Tasks(cid INTEGER PRIMARY KEY AUTOINCREMENT, nom text, Date text, Description text, Etat text)"
    cur.execute(query)

    conn.commit()

create_db()

