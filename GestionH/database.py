import sqlite3

def baseDonne():
    conn = sqlite3.connect(database="Hotel_management.db")
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS client(Ref INTEGER PRIMARY KEY AUTOINCREMENT, Nom varchar(45), Prenom varchar(45), Sexe	varchar(45), Contacte varchar(45), Email varchar(60), Nationnalité varchar(45), Piece varchar(45), Num_Piece varchar(45), Adresse varchar(60)"
    # query1 = "CREATE TABLE IF NOT EXISTS chambre(contact varchar(45), date_arrivee varchar(45), date_depart	varchar(45), type_chambre varchar(45), chambre_dispo INTEGER PRIMARY KEY, repas	varchar(45), nbr_jours	varchar(45), taxe_paye	varchar(45), sous_total	varchar(45), cout_total	varchar(45)"
    # query2 = "CREATE TABLE IF NOT EXISTS detail(Etage varchar(45), ChambreNum varchar(45) PRIMARY KEY, TypeDeChambre varchar(45)"
    cur.execute(query)

    conn.commit()
baseDonne()