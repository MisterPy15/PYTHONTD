import sqlite3

def create_db():

    conn = sqlite3.connect(database="school_managment.db")
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS Cours(cid INTEGER PRIMARY KEY AUTOINCREMENT, nom text, Durée text, Charge text, Description text)"
    query1 = "CREATE TABLE IF NOT EXISTS Etudiants(NumMat TEXT PRIMARY KEY, Nom text, Prenom text, Email text, Sexe text, DateNaiss text, Contact text, Cours_Select text, Date_Admission text, Niveau text, Ville text, Pin text, Adresse text)"
    cur.execute(query1)

    conn.commit()
create_db()