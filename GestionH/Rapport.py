from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ct
from tkinter import ttk
from time import strftime
from datetime import datetime
import pymysql
from tkinter import messagebox




class Rapport_fenetre:
    

    def __init__(self,mac):
        self.mac = mac
        self.mac.title("Gestion D'Hotel façon Mister Py 🐍")
        self.mac.geometry("1100x560+245+200")
        self.mac.resizable(0,0)


        # ===========================Label Titre=====================
        labelTitle = Label(self.mac, text="RAPPORT", font=('sans serif', 18, 'bold'), bg="black", fg="white", bd=4, relief=RIDGE)
        labelTitle.place(x=0, y=0,  width=1100, height=40)


        # ==============================Image Logo=========================
        img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        img2 = img2.resize((40, 30))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimage = Label(self.mac, image=self.photoimg2, bd=0, relief="ridge")
        labelimage.place(x=5, y=5, width=40, height=30)



        # =======================Label Frame===========
        labelFrameLeft = LabelFrame(self.mac, text="INFO DU CLIENT",bd=2, relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        labelFrameLeft.place(x=5, y=60, width=350, height=450)

        label_CLient_Ref = Label(labelFrameLeft, text="Ref client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Ref.grid(row=0, column=0)
        entry_Client_Ref = ct.CTkEntry(labelFrameLeft, width=150, font=("sans serif", 12, 'bold'), placeholder_text="Entrez la référence du client")
        entry_Client_Ref.grid(row=0, column=1, sticky=W)
        # button_Client_Check = ct.CTkButton(labelFrameLeft, text="Check", width=100)



        label_CLient_Nom = Label(labelFrameLeft, text="Nom client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Nom.grid(row=1, column=0)
        entry_Client_Nom = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'), placeholder_text="Nom")
        entry_Client_Nom.grid(row=1, column=1, sticky=W)



        label_CLient_Prenom = Label(labelFrameLeft, text="Prenom client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Prenom.grid(row=2, column=0)
        entry_Client_Prenom = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'))
        entry_Client_Prenom.grid(row=2, column=1, sticky=W)



        label_CLient_Sexe = Label(labelFrameLeft, text="Sexe", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Sexe.grid(row=3, column=0)

        option_Sexe = ct.CTkOptionMenu(labelFrameLeft,width=200,
                                                       values=["Homme", "Femme", "Autre"])
        option_Sexe.set("Homme")
        option_Sexe.grid(row=3, column=1, sticky=W)

        

        label_CLient_Nationnalite = Label(labelFrameLeft, text="Nationnalité", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Nationnalite.grid(row=4, column=0)

        option_CLient_Nationnalite = ct.CTkOptionMenu(labelFrameLeft,width=200,
                                                                      values=["Ivoirien", "Américain", "Français","Ghanéen"])
        option_CLient_Nationnalite.set("Ivoirien")
        option_CLient_Nationnalite.grid(row=4, column=1, sticky=W)



      
       



      


        # ====================Date D'arriver====================
        label_Date_Arrive = Label(labelFrameLeft, text="Date d'arrivée", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Date_Arrive.grid(row=5, column=0)
        entry_date_arrive = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'))
        entry_date_arrive.grid(row=5, column=1, sticky=W)


        



        # ====================Date====================
        label_Date_Depart = Label(labelFrameLeft, text="Date de départ", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Date_Depart.grid(row=6, column=0)
        entry_Date_Depart = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'))
        entry_Date_Depart.grid(row=6, column=1, sticky=W)



        # ==================== Nombre de jour ====================
        label_Nbr_jr = Label(labelFrameLeft, text="Nombres de Jours", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Nbr_jr.grid(row=7, column=0)
        entry_Nbr_jr = ct.CTkEntry(labelFrameLeft,width=200, font=("sans serif", 12, 'bold'))
        entry_Nbr_jr.grid(row=7, column=1, sticky=W)




        label_type_chambre = Label(labelFrameLeft, text="Type de chambre: ", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_type_chambre.grid(row=8, column=0)

        combo_type_chambre = ttk.Combobox(labelFrameLeft,
                                                        font=("sans serif", 12, 'bold'), foreground="black", state="readonly")
        combo_type_chambre["value"]=("Luxe", "Célibataire", "Pour deux")
        combo_type_chambre.grid(row=8, column=1)



        label_chambre_dispo = Label(labelFrameLeft, text="Chambre Nº", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_chambre_dispo.grid(row=9, column=0)

        combo_chambreNum = ttk.Combobox(labelFrameLeft, font=("sans serif", 12, 'bold'), foreground="black", state="readonly")
        combo_chambreNum["value"]=("")
        combo_chambreNum.grid(row=9, column=1)


         # ==================== Taxe Payé ====================
        label_Taxe_paye = Label(labelFrameLeft, text="Taxe Payé", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Taxe_paye.grid(row=10, column=0)
        entry_Taxe_paye = ct.CTkEntry(labelFrameLeft,width=200, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Taxe_paye.grid(row=10, column=1, sticky=W)


        # ==================== Sous Total ====================
        label_Sous_total = Label(labelFrameLeft, text="Total Actuel", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Sous_total.grid(row=11, column=0)
        entry_Sous_total = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Sous_total.grid(row=11, column=1, sticky=W)



        # ==================== cout Total ====================
        label_Cout_total = Label(labelFrameLeft, text="Coût Total", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Cout_total.grid(row=12, column=0)
        entry_Cout_total = ct.CTkEntry(labelFrameLeft, width=200, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Cout_total.grid(row=12, column=1, sticky=W)
        






        labelFrameRight = ct.CTkFrame(self.mac, border_width=7,corner_radius=20, width=550, height=450)
        labelFrameRight.place(x=400, y=60)

        text_frame = Label(labelFrameRight, text="Facture", font=('sans serif', 15, 'bold'), bg="black", fg="white", bd=6, relief=RIDGE)
        text_frame.place(x=0, y=15, width=545, height=45)




        buttonFrame = ct.CTkFrame(labelFrameRight, corner_radius=20, width=450, height=30)
        buttonFrame.place(x=40, y=390)

        button_Rapport = ct.CTkButton(buttonFrame, text="Rapport", corner_radius=20)
        button_Rapport.grid(row=0, column=0, padx=7)

        button_Rapport = ct.CTkButton(buttonFrame, text="Imprimer", corner_radius=20)
        button_Rapport.grid(row=0, column=1, padx=7)

        button_Rapport = ct.CTkButton(buttonFrame, text="Ouvrir", corner_radius=20)
        button_Rapport.grid(row=0, column=2, padx=7)




        txtfact = Text(labelFrameRight, font=("Times New Roman ", 13))
        txtfact.insert(END, " Réf : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Nom : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Prénom : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Sexe : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Nationnalité : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Date d'arrivée : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Date de Départ : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Nombre de jour : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Type de Chambre : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Chambre Nº : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Taxe payé : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Total actuel : ")
        txtfact.insert(END, " \n")
        txtfact.insert(END, " \n Coût Total : ")
        txtfact.place(x=5, y=60, height=300, width=540)





if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Rapport_fenetre(Mac)
    Mac.mainloop()