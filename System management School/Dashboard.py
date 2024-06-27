from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from Cours import cour
from Etudiant import Etudiants
from Resultat import Resultats





ct.set_appearance_mode("System")
ct.set_default_color_theme("green")


class dash:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Système de Gestion des Etudiants UTA")
        self.mac.geometry("1300x1000+0")
        # self.mac.config(bg="white")



        # ======================Icons================

        # img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        # img2 = img2.resize((40, 30))
        # self.photoimg2 = ImageTk.PhotoImage(img2)

            
        logoleft = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/System management School/images/logoP.webp")
        logoleft = logoleft.resize((50, 50))
        self.logo_dash = ImageTk.PhotoImage(logoleft)

        # ===================Titre==================
        title = ct.CTkLabel(self.mac, text="Système De Gestion Des Étudiants UTA",height=50, width=1300, 
                                      image=self.logo_dash, padx=10,  compound=LEFT,font=("goudy old style",
                                      20, "bold"), bg_color="#033054", fg_color="green")
        title.place(x=0, y=0)

        M_Frame = LabelFrame(self.mac, text="Menu", font=("sans serif", 15, "bold"))
        M_Frame.place(x=120, y=60, width=1100, height=60)

        button_course = ct.CTkButton(M_Frame, text="Cours", font=("goudy old style",12, "bold"), command=self.cours, corner_radius=20, fg_color="green")
        button_course.grid(row=0, column=0, padx=5)

        button_Etudiant = ct.CTkButton(M_Frame, text="Etudiant", font=("goudy old style",12, "bold"), command=self.Etudiant, corner_radius=20, fg_color="white", text_color="green")
        button_Etudiant.grid(row=0, column=1, padx=8)

        button_Résultat = ct.CTkButton(M_Frame, text="Résultat", font=("goudy old style",12, "bold"), corner_radius=20, command=self.Resultat, fg_color="green")
        button_Résultat.grid(row=0, column=2, padx=8)

        button_Résultat_Etu = ct.CTkButton(M_Frame, text="Résultat Etudiant", font=("goudy old style",12, "bold"), corner_radius=20, command=self.ResltEtu, fg_color="#342d7b")
        button_Résultat_Etu.grid(row=0, column=3, padx=8)

        button_Emploie_Du_temp = ct.CTkButton(M_Frame, text="Emploie Du temps", font=("goudy old style",12, "bold"), corner_radius=20, command=self.EmploiTemps, fg_color="white", text_color="#903997")
        button_Emploie_Du_temp.grid(row=0, column=4, padx=8)
        
        button_Deco = ct.CTkButton(M_Frame, text="Déconnexion", font=("goudy old style",12, "bold"), corner_radius=20, command=self.Deconnecion, fg_color="#903997")
        button_Deco.grid(row=0, column=5, padx=8)

        button_Quitter = ct.CTkButton(M_Frame, text="Quitter ->", font=("goudy old style",12, "bold"), corner_radius=20, command=self.Quitter, fg_color="red")
        button_Quitter.grid(row=0, column=6, padx=8)

        # ===============Content Window=========

        logoUTA = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/System management School/images/UTA.jpg")
        logoUTA = logoUTA.resize((300, 150))
        self.logo_UTA = ImageTk.PhotoImage(logoUTA)


        label_logoUTA = Label(self.mac, image=self.logo_UTA, width=300, height=150)
        label_logoUTA.place(x=50, y=180)


        logoISCAT = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/System management School/images/ISCAT.jpg")
        logoISCAT = logoISCAT.resize((300, 150))
        self.logo_ISCAT = ImageTk.PhotoImage(logoISCAT)


        label_logoISCAT = Label(self.mac, image=self.logo_ISCAT, width=300, height=150)
        label_logoISCAT.place(x=50, y=380)




        logoCenter = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/System management School/images/Home.jpg")
        logoCenter = logoCenter.resize((920, 350))
        self.logo_center = ImageTk.PhotoImage(logoCenter)


        label_logoCenter = Label(self.mac, image=self.logo_center, width=920, height=350)
        label_logoCenter.place(x=350, y=180)


        # ==============Update deatails============
        self.label_cours = Label(self.mac,  text="Total de Cours\n[ 0 ]",bd=10, relief=RIDGE, 
                                            font=("goudy old style", 20), bg="green", fg="white")
        self.label_cours.place(x=350, y=530, width=300, height=100)


        self.label_Etudiant = Label(self.mac,  text="Total Etudiants\n[ 0 ]",bd=10, relief=RIDGE, 
                                            font=("goudy old style", 20), bg="white", fg="green")
        self.label_Etudiant.place(x=660, y=530, width=300, height=100)

        
        self.label_Resultat = Label(self.mac,  text="Total de Résultats\n[ 0 ]",bd=10, relief=RIDGE, 
                                            font=("goudy old style", 20), bg="green", fg="white")
        self.label_Resultat.place(x=970, y=530, width=300, height=100)


        # ======================footer====================
        footer_label = ct.CTkLabel(self.mac,    text="Système de gestion des Etudiants UTA\n Contactez Mister Py🐍 : 0778748602", 
                                                font=("goudy old style",12, "bold"), bg_color="#033054", fg_color="green")
        footer_label.pack(side=BOTTOM, fill=X)




 


    def cours(self):
        self.Cour = Toplevel(self.mac)
        self.app = cour(self.Cour)

    def Etudiant(self):
        self.Etudiant = Toplevel(self.mac)
        self.app = Etudiants(self.Etudiant)

    def Resultat(self):
        self.Resultat = Toplevel(self.mac)
        self.app = Resultats(self.Resultat)
    
    def ResltEtu(self):
        pass
    
    def EmploiTemps(self):
        pass

    def Deconnecion(self):
        pass

    def Quitter(self):
        self.mac.destroy()






if __name__ == "__main__":
    Mac = ct.CTk()
    obj = dash(Mac)
    Mac.mainloop()