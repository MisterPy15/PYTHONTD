import sqlite3

def create_db():

    conn = sqlite3.connect(database="GestionTache.db")
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS ToDo(Tache text, date text, description text, valider text)"
    cur.execute(query)

    conn.commit()

create_db()

