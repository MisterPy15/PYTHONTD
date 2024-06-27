from tkinter import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter  # Importe la taille de page "letter"
import os
import subprocess
import sysw

def generer_recu():
    nom_client = nom_entry.get()
    montant = montant_entry.get()

    # Créer un nouveau fichier PDF pour le reçu avec une taille spécifique
    nom_fichier = f"{nom_client}_recu.pdf"
    pdf = canvas.Canvas(nom_fichier, pagesize=letter)  # Utilise la taille de page "letter"

    # Écrire les détails du reçu dans le fichier PDF
    pdf.drawString(100, 750, "Reçu")
    pdf.drawString(100, 730, f"Nom du client : {nom_client}")
    pdf.drawString(100, 710, f"Montant : {montant} $")
    pdf.save()

    # Afficher un message de confirmation
    confirmation_label.config(text="Reçu généré avec succès!")

# Interface graphique avec Tkinter
root = Tk()
root.title("Générateur de reçu")

label_nom = Label(root, text="Nom du client :")
label_nom.pack()

nom_entry = Entry(root)
nom_entry.pack()

label_montant = Label(root, text="Montant :")
label_montant.pack()

montant_entry = Entry(root)
montant_entry.pack()

confirmation_label = Label(root, text="")
confirmation_label.pack()

def imprimer_recu():
    nom_client = nom_entry.get()
    nom_fichier = f"{nom_client}_recu.pdf"

    # Vérifier si le fichier existe avant de l'imprimer
    if os.path.exists(nom_fichier):
        if sys.platform.startswith('win'):
            subprocess.run(["start", "/B", "AcroRd32", "/p", nom_fichier], shell=True)
        elif sys.platform.startswith('linux'):
            subprocess.run(["xdg-open", nom_fichier])
        elif sys.platform == "darwin":
            subprocess.run(["open", nom_fichier])
        else:
            confirmation_label.config(text="Impossible d'imprimer sur cette plateforme.")
    else:
        confirmation_label.config(text="Le fichier n'existe pas.")

# Bouton pour générer le reçu
generer_button = Button(root, text="Générer reçu", command=generer_recu)
generer_button.pack()

# Bouton pour imprimer le reçu
imprimer_button = Button(root, text="Imprimer reçu", command=imprimer_recu)
imprimer_button.pack()

root.mainloop()
