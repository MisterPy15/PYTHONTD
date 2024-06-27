# import tkinter as tk

# def scroll_text():
#     global text
#     text = text[1:] + text[0]  # Déplacer le premier caractère à la fin
#     label.config(text=text)
#     label.after(100, scroll_text)  # Appeler cette fonction toutes les 100 millisecondes


# root = tk.Tk()
# root.title("Texte défilant")

# text = "Ceci est un texte défilant."
# label = tk.Label(root, text=text, font=("Arial", 12))
# label.pack()

# scroll_text()  # Lancer le défilement du texte

# root.mainloop()













# conn = pymysql.connect(
#                         host = "localhost",
#                         user = "root",
#                         password = "",
#                         database= "management"
#                     )

# mycursor = conn.cursor()
# query = "select ChambreNum from detail"
# mycursor.execute(query)
# rows = mycursor.fetchall()



# option_ChambreNum = ct.CTkOptionMenu(labelFrameLeft,width=200, variable=self.var_ChambreDispo, values=rows, state="readonly")
# option_ChambreNum.grid(row=4, column=1, sticky=W)




# import pymysql
# import tkinter as tk
# from tkinter import ttk

# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="management"
# )

# mycursor = conn.cursor()
# query = "SELECT ChambreNum FROM detail"
# mycursor.execute(query)
# rows = mycursor.fetchall()

# # Crée une liste de chaînes à partir des résultats de la requête
# chambre_nums = [row[0] for row in rows]

# root = tk.Tk()
# labelFrameLeft = ttk.LabelFrame(root, text="Chambres disponibles")
# labelFrameLeft.pack()

# var_ChambreDispo = tk.StringVar(root)
# var_ChambreDispo.set(chambre_nums[0])  # Sélectionnez par défaut le premier élément

# option_ChambreNum = ttk.Combobox(labelFrameLeft, width=200, textvariable=var_ChambreDispo, values=chambre_nums, state="readonly")
# option_ChambreNum.grid(row=4, column=1, sticky="w")

# root.mainloop()

















# import pymysql
# import customtkinter as ct

# conn = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="management"
# )

# mycursor = conn.cursor()
# query = "SELECT ChambreNum FROM detail"
# mycursor.execute(query)
# rows = mycursor.fetchall()

# # Crée une liste de chaînes à partir des résultats de la requête
# chambre_nums = [str(row[0]) for row in rows]

# root = ct.Tk()

# labelFrameLeft = ct.LabelFrame(root, text="Chambres disponibles")
# labelFrameLeft.pack()

# var_ChambreDispo = StringVar(root)
# var_ChambreDispo.set(chambre_nums[0])  # Sélectionnez par défaut le premier élément

# option_ChambreNum = ct.CTkOptionMenu(labelFrameLeft, width=200, variable=var_ChambreDispo, values=chambre_nums)
# option_ChambreNum.grid(row=4, column=1, sticky="w")

# root.mainloop()













# def impression(self):
#     fichier = tempfile.mktemp(".txt")
#     open(fichier, "w").write(self.textarea.get)










# import tkinter as tk

# class GestionNotesUTA:
#     def __init__(self):
#         self.etudiants = {}

#     def ajouter_etudiant(self, nom, matricule):
#         if matricule not in self.etudiants:
#             self.etudiants[matricule] = {'nom': nom, 'notes': []}
#             print(f"Étudiant {nom} ajouté avec succès!")
#         else:
#             print("L'étudiant existe déjà.")

#     def ajouter_note(self, matricule, note):
#         if matricule in self.etudiants:
#             self.etudiants[matricule]['notes'].append(note)
#             print(f"Note ajoutée pour l'étudiant {self.etudiants[matricule]['nom']}")
#         else:
#             print("Matricule d'étudiant invalide.")

#     def moyenne_etudiant(self, matricule):
#         if matricule in self.etudiants:
#             notes = self.etudiants[matricule]['notes']
#             if notes:
#                 moyenne = sum(notes) / len(notes)
#                 return moyenne
#             else:
#                 return "Aucune note disponible pour cet étudiant."
#         else:
#             return "Matricule d'étudiant invalide."

#     def moyenne_classe(self):
#         all_notes = []
#         for etudiant in self.etudiants.values():
#             all_notes.extend(etudiant['notes'])
#         if all_notes:
#             moyenne = sum(all_notes) / len(all_notes)
#             return moyenne
#         else:
#             return "Aucune note disponible pour calculer la moyenne de la classe."

# # Interface utilisateur avec tkinter
# class InterfaceUtilisateur:
#     def __init__(self, fenetre):
#         self.fenetre = fenetre
#         self.fenetre.title("Gestionnaire de notes UTA")

#         self.label_nom = tk.Label(fenetre, text="Nom de l'étudiant:")
#         self.label_nom.pack()
#         self.entry_nom = tk.Entry(fenetre)
#         self.entry_nom.pack()

#         self.label_matricule = tk.Label(fenetre, text="Matricule de l'étudiant:")
#         self.label_matricule.pack()
#         self.entry_matricule = tk.Entry(fenetre)
#         self.entry_matricule.pack()

#         self.label_note = tk.Label(fenetre, text="Note de l'étudiant:")
#         self.label_note.pack()
#         self.entry_note = tk.Entry(fenetre)
#         self.entry_note.pack()

#         self.bouton_ajouter_etudiant = tk.Button(fenetre, text="Ajouter étudiant", command=self.ajouter_etudiant)
#         self.bouton_ajouter_etudiant.pack()

#         self.bouton_ajouter_note = tk.Button(fenetre, text="Ajouter note", command=self.ajouter_note)
#         self.bouton_ajouter_note.pack()

#         self.bouton_moyenne_etudiant = tk.Button(fenetre, text="Moyenne de l'étudiant", command=self.moyenne_etudiant)
#         self.bouton_moyenne_etudiant.pack()

#         self.bouton_moyenne_classe = tk.Button(fenetre, text="Moyenne de la classe", command=self.moyenne_classe)
#         self.bouton_moyenne_classe.pack()

#         self.textbox = tk.Text(fenetre)
#         self.textbox.pack()

#         self.gestion_notes = GestionNotesUTA()

#     def ajouter_etudiant(self):
#         nom = self.entry_nom.get()
#         matricule = self.entry_matricule.get()
#         self.gestion_notes.ajouter_etudiant(nom, matricule)
#         self.textbox.insert(tk.END, f"Étudiant {nom} ajouté avec succès!\n")

#     def ajouter_note(self):
#         matricule = self.entry_matricule.get()
#         note = float(self.entry_note.get())
#         self.gestion_notes.ajouter_note(matricule, note)
#         self.textbox.insert(tk.END, f"Note ajoutée pour l'étudiant {self.gestion_notes.etudiants[matricule]['nom']}\n")

#     def moyenne_etudiant(self):
#         matricule = self.entry_matricule.get()
#         moyenne = self.gestion_notes.moyenne_etudiant(matricule)
#         self.textbox.insert(tk.END, f"Moyenne de l'étudiant : {moyenne}\n")

#     def moyenne_classe(self):
#         moyenne = self.gestion_notes.moyenne_classe()
#         self.textbox.insert(tk.END, f"Moyenne de la classe : {moyenne}\n", state="readonly")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = InterfaceUtilisateur(root)
#     root.mainloop()








import tkinter as tk
import pymysql
from reportlab.pdfgen import canvas
from datetime import datetime
conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )
mycursor = conn.cursor()


mycursor.execute()
conn.commit()
conn.close()
def generer():
    code_reference = int(code_reference_entry.get())
    mycursor.execute("SELECT * FROM clients WHERE code_reference=?", (code_reference,))
    row = mycursor.fetchone()
    if row:
        nom_entry.insert(0, row[1])
        prenom_entry.insert(0, row[2])
        sexe_entry.insert(0, row[3])
        nationalite_entry.insert(0, row[4])
        date_arrivee_entry.insert(0, row[5])
        date_depart_entry.insert(0, row[6])
        nb_jours_entry.insert(0, row[7])
        type_chambre_entry.insert(0, row[8])
        num_chambre_entry.insert(0, row[9])
        tva_entry.insert(0, row[10])
        total_brut_entry.insert(0, row[11])
        total_net_entry.insert(0, row[12])
    else:
        print("Code de référence invalide")

def generer_pdf():
    code_reference = int(code_reference_entry.get())
    mycursor.execute("SELECT * FROM clients WHERE code_reference=?", (code_reference,))
    row = mycursor.fetchone()
    if row:
        filename = f"facture_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        mycursor = canvas.Canvas(filename)
        # Génération du contenu du PDF avec les valeurs de la base de données
        mycursor.drawString(100, 700, f"Nom : {row[1]}")
        # Ajoutez d'autres données de la même manière
        mycursor.save()
        print(f"Facture générée : {filename}")
    else:
        print("Code de référence invalide")

def ouvrir_pdf():
    generer_pdf()
    # Code pour ouvrir le PDF généré automatiquement

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de reçu pour l'hôtel")

# Création des champs de texte et des boutons (à compléter de manière similaire à l'exemple précédent)

root.mainloop()