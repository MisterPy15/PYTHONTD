from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import random as rd




ct.set_appearance_mode("System")
ct.set_default_color_theme("green")



class Resultats:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Système de Gestion des Etudiants UTA")
        self.mac.geometry("1200x535+80+170")
       

        

        # ===================Titre==================
        title = ct.CTkLabel(self.mac, text="Ajout Des Resultats Des Etudiants", height=35, width=1180, 
                                      padx=10, compound=LEFT, font=("goudy old style",20, "bold"),
                                      bg_color="#033054", fg_color="green")
        title.place(x=10, y=15)



        # ==========================Label Column1======================
        label_Etudiant = ct.CTkLabel(self.mac, text="Etudiant", font=("sans serif", 15, "bold"))
        label_Etudiant.place(x=40, y=80)

        buttonSearch = ct.CTkButton(self.mac, text="Rechercher", text_color="white",font=("sans serif", 12, "bold"),fg_color="green", command=self.search,
                                                    corner_radius=20, width=110)
        buttonSearch.place(x=300, y=80)


        label_Nom = ct.CTkLabel(self.mac, text="Nom", font=("sans serif", 15, "bold"))
        label_Nom.place(x=40, y=120)

        label_Prenom = ct.CTkLabel(self.mac, text="Prenom", font=("sans serif", 15, "bold"))
        label_Prenom.place(x=40, y=160)

        label_Cour = ct.CTkLabel(self.mac, text="Cour", font=("sans serif", 15, "bold"))
        label_Cour.place(x=40, y=200)

        label_Note = ct.CTkLabel(self.mac, text="Note Obtenu", font=("sans serif", 15, "bold"))
        label_Note.place(x=40, y=240)

        label_Total = ct.CTkLabel(self.mac, text="Total", font=("sans serif", 15, "bold"))
        label_Total.place(x=40, y=280)


        # ================================Entry===================================

        # self.txt_Etudiant= ct.CTkEntry(self.mac, placeholder_text="Nº Matricule", font=("sans serif", 15, "bold"), width=150)
        # self.txt_Etudiant.place(x=150, y=80)
        self.var_Pin = StringVar()
        self.var_Nom = StringVar()
        self.var_Prenom = StringVar()
        self.var_Cour = StringVar()
        self.var_Note = StringVar()
        self.var_noteTotal = StringVar()
        # self.Pin_list = []
        # self.fetch_NumMat()

        conn = sqlite3.connect(database="school_managment.db")
        cur = conn.cursor()
        query = "select Pin from Etudiants"
        cur.execute(query)
        rows = cur.fetchall()

        self.txt_Etudiant = ct.CTkOptionMenu(self.mac, variable=self.var_Pin, values=[row[0] for row in rows])
        self.txt_Etudiant.place(x=150, y=80)

        txt_Nom = ct.CTkEntry(self.mac, textvariable=self.var_Nom, font=("sans serif", 15, "bold"), width=300, state="readonly")
        txt_Nom.place(x=150, y=120)

        txt_Prenom = ct.CTkEntry(self.mac, textvariable=self.var_Prenom, font=("sans serif", 15, "bold"), width=300, state="readonly")
        txt_Prenom.place(x=150, y=160)

        txt_Cour = ct.CTkEntry(self.mac, textvariable=self.var_Cour, placeholder_text="Entrez la durée", font=("sans serif", 13, "bold"), width=300, state="readonly")
        txt_Cour.place(x=150, y=200)

        txt_Note = ct.CTkEntry(self.mac, textvariable=self.var_Note, placeholder_text="Entrez la durée", font=("sans serif", 13, "bold"), width=300, state="readonly")
        txt_Note.place(x=150, y=240)

        txt_Total = ct.CTkEntry(self.mac, textvariable=self.var_noteTotal, placeholder_text="Entrez la durée", font=("sans serif", 13, "bold"), width=300, state="readonly")
        txt_Total.place(x=150, y=280)


        # =========== buttons ===================
        self.buttonSubmit = ct.CTkButton(self.mac, text="Envoie",text_color="green", font=("sans serif", 12, "bold"),fg_color="white",
                                                  corner_radius=20, width=110)
        self.buttonSubmit.place(x=200, y=350)

        self.buttonClear = ct.CTkButton(self.mac, text="Effacer",text_color="white", font=("sans serif", 12, "bold"),fg_color="green",
                                                  corner_radius=20, width=110)
        self.buttonClear.place(x=320, y=350)


        # label image

        ResultImage = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/System management School/images/R3.jpeg")
        ResultImage = ResultImage.resize((650, 400))
        self.logo_Result = ImageTk.PhotoImage(ResultImage)

        title = ct.CTkLabel(self.mac, text=None, width=650, height=400, image=self.logo_Result, padx=10)
        title.place(x=480, y=80)


    # def fetch_NumMat(self):
    #         conn = sqlite3.connect(database="school_managment.db")
    #         cur = conn.cursor()
    #         try:
    #             query = "select Pin from Etudiants"
    #             cur.execute(query)
    #             rows = cur.fetchall()
    #             if len(rows)>0:
    #                 for row in rows:
    #                     self.Pin_list.append(row[0])
    #         except Exception as ex:
    #             messagebox.showerror("Erreur", f"Erreur dû à {str(ex)}")



    def search(self):
        conn = sqlite3.connect(database="school_managment.db")
        cur = conn.cursor()

        try:
            query = "SELECT Nom, Prenom, Cours_Select FROM Etudiants WHERE Pin=?"
            search_term = self.var_Pin.get()
            cur.execute(query, (search_term,))
            rows = cur.fetchone()   
            if rows != None:
                self.var_Nom.set(rows[0])
                self.var_Prenom.set(rows[1])
                self.var_Note.set(rows[2])
                self.var_Cour.set(rows[3])
                self.var_noteTotal.set(rows[4])
            else:
                messagebox.showerror("Erreur", "Introuvable", parent=self.mac)

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à {str(ex)}", parent=self.mac)





if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Resultats(Mac)
    Mac.mainloop()


































#    ______
#   / ____/___  ____ ___  ____  ____  ________  _____
#  / /   / __ \/ __ `__ \/ __ \/ __ \/ ___/ _ \/ ___/
# / /___/ /_/ / / / / / / /_/ / /_/ (__  )  __/ /
# \____/\____/_/ /_/ /_/ .___/\____/____/\___/_/
#                     /_/
