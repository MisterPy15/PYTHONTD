import tkinter as tk
import customtkinter as ct



class GestionNotesUTA:
    def __init__(self):
        self.etudiants = {}

    def ajouter_etudiant(self, nom, matricule):
        if matricule not in self.etudiants:
            self.etudiants[matricule] = {'nom': nom, 'notes': []}
            print(f"Étudiant {nom} ajouté avec succès!")
        else:
            print("L'étudiant existe déjà.")

    def ajouter_note(self, matricule, note):
        if matricule in self.etudiants:
            self.etudiants[matricule]['notes'].append(note)
            print(f"Note ajoutée pour l'étudiant {self.etudiants[matricule]['nom']}")
        else:
            print("Matricule d'étudiant invalide.")

    def moyenne_etudiant(self, matricule):
        if matricule in self.etudiants:
            notes = self.etudiants[matricule]['notes']
            if notes:
                moyenne = sum(notes) / len(notes)
                return moyenne
            else:
                return "Aucune note disponible pour cet étudiant."
        else:
            return "Matricule d'étudiant invalide."

    def moyenne_classe(self):
        all_notes = []
        for etudiant in self.etudiants.values():
            all_notes.extend(etudiant['notes'])
        if all_notes:
            moyenne = sum(all_notes) / len(all_notes)
            return moyenne
        else:
            return "Aucune note disponible pour calculer la moyenne de la classe."

# Interface utilisateur avec tkinter
class InterfaceUtilisateur:

    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Gestionnaire de notes UTA")

        self.label_nom = ct.CTkLabel(fenetre, text="Nom de l'étudiant:")
        self.label_nom.grid(row=0, column=0)

        self.entry_nom = ct.CTkEntry(fenetre)
        self.entry_nom.grid(row=0, column=1)

        self.label_matricule = ct.CTkLabel(fenetre, text="Matricule de l'étudiant:")
        self.label_matricule.grid(row=1, column=0)

        self.entry_matricule = ct.CTkEntry(fenetre)
        self.entry_matricule.grid(row=1, column=1)

        self.label_note = ct.CTkLabel(fenetre, text="Note de l'étudiant:")
        self.label_note.grid(row=2, column=0)
        self.entry_note = ct.CTkEntry(fenetre)
        self.entry_note.grid(row=2, column=1)



        self.bouton_ajouter_etudiant = ct.CTkButton(fenetre, text="Ajouter étudiant", command=self.ajouter_etudiant)
        self.bouton_ajouter_etudiant.place(relx=30, rely=200)

        self.bouton_ajouter_note = tk.Button(fenetre, text="Ajouter note", command=self.ajouter_note)
        self.bouton_ajouter_note.pack()

        self.bouton_moyenne_etudiant = tk.Button(fenetre, text="Moyenne de l'étudiant", command=self.moyenne_etudiant)
        self.bouton_moyenne_etudiant.pack()

        self.bouton_moyenne_classe = tk.Button(fenetre, text="Moyenne de la classe", command=self.moyenne_classe)
        self.bouton_moyenne_classe.pack()

        self.textbox = tk.Text(fenetre)
        self.textbox.pack()

        self.gestion_notes = GestionNotesUTA()

    def ajouter_etudiant(self):
        nom = self.entry_nom.get()
        matricule = self.entry_matricule.get()
        self.gestion_notes.ajouter_etudiant(nom, matricule)
        self.textbox.insert(tk.END, f"Étudiant {nom} ajouté avec succès!\n")

    def ajouter_note(self):
        matricule = self.entry_matricule.get()
        note = float(self.entry_note.get())
        self.gestion_notes.ajouter_note(matricule, note)
        self.textbox.insert(tk.END, f"Note ajoutée pour l'étudiant {self.gestion_notes.etudiants[matricule]['nom']}\n")

    def moyenne_etudiant(self):
        matricule = self.entry_matricule.get()
        moyenne = self.gestion_notes.moyenne_etudiant(matricule)
        self.textbox.insert(tk.END, f"Moyenne de l'étudiant : {moyenne}\n")

    def moyenne_classe(self):
        moyenne = self.gestion_notes.moyenne_classe()
        self.textbox.insert(tk.END, f"Moyenne de la classe : {moyenne}\n", state="readonly")


if __name__ == "__main__":
    root = ct.CTk()
    app = InterfaceUtilisateur(root)
    root.mainloop()