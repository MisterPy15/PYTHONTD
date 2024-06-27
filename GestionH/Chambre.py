from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ct
from tkinter import ttk
from time import strftime
from datetime import datetime
from tkcalendar import *
import pymysql
from tkinter import messagebox





class chambre_fenetre:
    

    def __init__(self,mac):
        self.mac = mac
        self.mac.title("Gestion D'Hotel façon Mister Py 🐍")
        self.mac.geometry("1100x540+245+180")
        self.mac.resizable(0,0)



        # =======================Variables====================

        self.var_contact = StringVar()
        self.var_dateArrive = StringVar()
        self.var_DateDepart = StringVar()
        self.var_TypeChambre = StringVar()
        self.var_ChambreDispo = StringVar()
        self.var_repas = StringVar()
        self.var_NbrJours = StringVar()
        self.var_TaxePaye = StringVar()
        self.var_SousTotal = StringVar()
        self.var_coutTotal = StringVar()





        # ===========================Label Titre=====================
        labelTitle = Label(self.mac, text="RESERVATION DE CHAMBRE", font=('sans serif', 18, 'bold'), bg="black", fg="white", bd=4, relief=RIDGE)
        labelTitle.place(x=0, y=0, width=1100, height=40)



        # ==============================Image Logo=========================
        img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        img2 = img2.resize((40, 30))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimage = Label(self.mac, image=self.photoimg2, bd=0, relief="ridge")
        labelimage.place(x=5, y=5, width=40, height=30)

        # =======================Label Frame===========
        labelFrameLeft = LabelFrame(self.mac, text="Détails de la chambre a réservé",bd=2, relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        labelFrameLeft.place(x=5, y=40, width=350, height=490)



        # ====================== Contacte client ============

        label_CLient_Contacte = Label(labelFrameLeft, text="Contact Client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Contacte.grid(row=0, column=0)
        entry_Contacte = ct.CTkEntry(labelFrameLeft, width=150, textvariable=self.var_contact, font=("sans serif", 12, 'bold'))
        entry_Contacte.grid(row=0, column=1, sticky=W)


        btn_Recup_Donnee = ct.CTkButton(labelFrameLeft, text="Check", command=self.Check,
                                            font=("sans serif", 7, 'bold'), text_color="white", 
                                            fg_color="black" , cursor="hand1",corner_radius=20, width=2)
        btn_Recup_Donnee.place(x=285, y=0)


        # ====================Date D'arriver====================
        label_Date_Arrive = Label(labelFrameLeft, text="Date d'arrivée", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Date_Arrive.grid(row=1, column=0)
        entry_date_arrive = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_dateArrive, font=("sans serif", 12, 'bold'))
        entry_date_arrive.grid(row=1, column=1, sticky=W)

        # entry_date_arrive = DateEntry(ctentry_date_arrive,width=18, font=("sans serif", 12, 'bold'), fg="black", state="readonly", bg="black", date_pattern="dd/mm/yy")
        # entry_date_arrive.grid(row=0, column=0)
        

        



        # ====================Date====================
        label_Date_Depart = Label(labelFrameLeft, text="Date de départ", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Date_Depart.grid(row=2, column=0)
        entry_Date_Depart = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_DateDepart, font=("sans serif", 12, 'bold'))
        entry_Date_Depart.grid(row=2, column=1, sticky=W)


        # ====================chambre====================
        
        conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )

        mycursor = conn.cursor()
        query = "select TypeDeChambre from detail"
        mycursor.execute(query)
        ide = mycursor.fetchall()



        label_type_chambre = Label(labelFrameLeft, text="Type de chambre: ", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_type_chambre.grid(row=3, column=0)

        # combo_type_chambre = ttk.Combobox(labelFrameLeft, textvariable=self.var_TypeChambre,
        #                                                 font=("sans serif", 12, 'bold'), foreground="black", state="readonly")
        # combo_type_chambre["value"]=ide
        # combo_type_chambre.grid(row=3, column=1)


        option_type_chambre = ct.CTkOptionMenu(labelFrameLeft, width=200, variable=self.var_TypeChambre,
                                                               values=[ides[0] for ides in ide])
        option_type_chambre.grid(row=3, column=1, sticky=W)



        #============================= Chambre dispo ========================
        conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )
        mycursor = conn.cursor()
        query = "select ChambreNum from detail"
        mycursor.execute(query)
        rows = mycursor.fetchall()



        label_chambre_dispo = Label(labelFrameLeft, text="Chambre Disponible", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_chambre_dispo.grid(row=4, column=0)

        # combo_chambreNum = ttk.Combobox(labelFrameLeft, textvariable=self.var_ChambreDispo, font=("sans serif", 12, 'bold'), foreground="black", state="readonly")
        # combo_chambreNum["value"]=rows
        # combo_chambreNum.grid(row=4, column=1)

        # entry_chambre_dispo = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_ChambreDispo, font=("sans serif", 12, 'bold'))
        # entry_chambre_dispo.grid(row=4, column=1, sticky=W)

        option_ChambreNum = ct.CTkOptionMenu(labelFrameLeft,width=200, variable=self.var_ChambreDispo, values=[row[0] for row in rows])
        option_ChambreNum.grid(row=4, column=1, sticky=W)




       
        # ====================Repas====================
        label_repas = Label(labelFrameLeft, text="Repas", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_repas.grid(row=5, column=0)
        option_CLient_repas = ct.CTkOptionMenu(labelFrameLeft,  width=200, variable=self.var_repas, 
                                                                values=["Petit Déjeuné", "Déjeuné", "Diné", "Les Trois Repas"], state="readonly")
        option_CLient_repas.grid(row=5, column=1, sticky=W)


        # ==================== Nombre de jour ====================
        label_Nbr_jr = Label(labelFrameLeft, text="Nombres de Jours", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Nbr_jr.grid(row=6, column=0)
        entry_Nbr_jr = ct.CTkEntry(labelFrameLeft,width=200, textvariable=self.var_NbrJours, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Nbr_jr.grid(row=6, column=1, sticky=W)

        # ==================== Taxe Payé ====================
        label_Taxe_paye = Label(labelFrameLeft, text="Taxe Payé", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Taxe_paye.grid(row=7, column=0)
        entry_Taxe_paye = ct.CTkEntry(labelFrameLeft,width=200, textvariable=self.var_TaxePaye,font=("sans serif", 12, 'bold'), state="readonly")
        entry_Taxe_paye.grid(row=7, column=1, sticky=W)


        # ==================== Sous Total ====================
        label_Sous_total = Label(labelFrameLeft, text="Total Actuel", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Sous_total.grid(row=8, column=0)
        entry_Sous_total = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_SousTotal,font=("sans serif", 12, 'bold'), state="readonly")
        entry_Sous_total.grid(row=8, column=1, sticky=W)



        # ==================== cout Total ====================
        label_Cout_total = Label(labelFrameLeft, text="Coût Total", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_Cout_total.grid(row=9, column=0)
        entry_Cout_total = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_coutTotal, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Cout_total.grid(row=9, column=1, sticky=W)
        

        # ===============================Factur================================
        btn_Facture = ct.CTkButton(labelFrameLeft, text="Facture 🧾", command=self.total,
                                            font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" , cursor="hand1",corner_radius=20, width=5)
        btn_Facture.place(x=130, y=330)



        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=20, y=370, width=300, height=45)

        btn_Ajout = ct.CTkButton(btn_frame, text="Ajouter", command=self.add_data,
                                            font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" , cursor="hand1",corner_radius=20, width=5)
        btn_Ajout.grid(row=0, column=0, padx=4, pady=6)
        
        btn_MAJ = ct.CTkButton(btn_frame, text="Update",
                                          font=("sans serif", 10, 'bold'), text_color="white", command=self.Update,
                                          fg_color="black" ,cursor="hand1", corner_radius=20, width=5)
        btn_MAJ.grid(row=0, column=1,  padx=4, pady=6)

        btn_Suppr = ct.CTkButton(btn_frame, text="Effacer", command=self.mDelete,
                                            font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" ,cursor="hand1",corner_radius=20, width=5)
        btn_Suppr.grid(row=0, column=2, padx=4, pady=6)

        btn_Reset = ct.CTkButton(btn_frame, text="Reset", command=self.reset,
                                            font=("sans serif", 10, 'bold'), text_color="white", fg_color="black" ,
                                            cursor="hand1", corner_radius=20, width=5)
        btn_Reset.grid(row=0, column=3,  padx=4, pady=6)


        # ===================Image a droite========================
        img3 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/im2.jpg")
        img3 = img3.resize((320, 200))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labelimage = Label(self.mac, image=self.photoimg3, bd=0, relief=RIDGE)
        labelimage.place(x=710, y=55, width=300, height=200)



        # ====================Table Frame====================
        Table_frame = LabelFrame(self.mac, text="Vues des détails et Système de Recherche",bd=2, 
                                           relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        Table_frame.place(x=380, y=280, width=690, height=250)



        label_recherche = Label(Table_frame, text="Rechercher par: ",
                                             font=("sans serif", 12, 'bold'), bg="red", fg="#fff")
        label_recherche.grid(row=0, column=0, padx=2)


        self.var_recherche = StringVar()
        option_Recherche = ct.CTkOptionMenu(Table_frame, variable=self.var_recherche, width=150, values=["contact","chambre_dispo"])
        option_Recherche.set("chambre")
        option_Recherche.grid(row=0, column=1, sticky=W)



        self.txt_recherche = StringVar()
        entry_Recherche = ct.CTkEntry(Table_frame, width=150, textvariable=self.txt_recherche, font=("sans serif", 12, 'bold'))
        entry_Recherche.grid(row=0, column=2, padx=2, sticky=W)



        btn_Search =  ct.CTkButton(Table_frame, text="Search", command=self.search,
                                                font=("sans serif", 10, 'bold'), text_color="white",
                                                fg_color="black" , cursor="hand1", corner_radius=20, width=10)
        btn_Search.grid(row=0, column=3, padx=1)
        


        btn_Show_All = ct.CTkButton(Table_frame, text="Show All", command=self.feech_data,
                                                 font=("sans serif", 10, 'bold'), text_color="white", fg_color="black" , cursor="hand1", corner_radius=20, width=10)
        btn_Show_All.grid(row=0, column=4, padx=1)






        # ============================Show Data Table==================
        details_table = Frame(Table_frame, bd=2, relief=RIDGE, bg="black")
        details_table.place(x=0, y=50, width=685, height=175)

        Scroll_x = Scrollbar(details_table, orient=HORIZONTAL)
        Scroll_y = Scrollbar(details_table, orient=VERTICAL)


        self.chambre_Table = ttk.Treeview(details_table, column=("Contact", "DateArrive", "DateDepart", "TypeDeChambre", "ChambreDispo",
                                                                        "Repas", "NombreDeJours", "TaxePaye", "SousTotal", "CoutTotal"),
                                                                         xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.chambre_Table.xview)
        Scroll_y.config(command=self.chambre_Table.yview)

        self.chambre_Table.heading("Contact", text="Contacte")
        self.chambre_Table.heading("DateArrive", text="Date d'arrivée")
        self.chambre_Table.heading("DateDepart", text="Date de départ")
        self.chambre_Table.heading("TypeDeChambre", text="Type de Chambre")
        self.chambre_Table.heading("ChambreDispo", text="Chambre Disponible")
        self.chambre_Table.heading("Repas", text="Repas")
        self.chambre_Table.heading("NombreDeJours", text="Nombre De Jours")
        self.chambre_Table.heading("TaxePaye", text="Taxe Paye")
        self.chambre_Table.heading("SousTotal", text="Sous Total")
        self.chambre_Table.heading("CoutTotal", text="Cout Total")

        self.chambre_Table["show"]="headings"
        

        self.chambre_Table.column("Contact", width=100)
        self.chambre_Table.column("DateArrive", width=100)
        self.chambre_Table.column("DateDepart", width=100)
        self.chambre_Table.column("TypeDeChambre", width=100)
        self.chambre_Table.column("ChambreDispo", width=100)
        self.chambre_Table.column("Repas", width=100)
        self.chambre_Table.column("NombreDeJours", width=100)
        self.chambre_Table.column("TaxePaye", width=100)
        self.chambre_Table.column("SousTotal", width=100)
        self.chambre_Table.column("CoutTotal", width=100)


        self.chambre_Table.pack(fill=BOTH, expand=1)
        self.chambre_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.feech_data()





    def Check(self):
        if self.var_contact.get() =="":
            messagebox.showerror("Erreur", "SVP Entrez le contacte du client", parent=self.mac)
        else:
            conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
            mycursor = conn.cursor()
            query = ("select Nom from client where Contacte=%s")
            value = (self.var_contact.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Erreur", "Ce numéro est introuvable", parent=self.mac)
            else:
                conn.commit()
                conn.close()

                showDtatFrame = ct.CTkFrame(self.mac, bg_color="white", width=310, height=150, corner_radius=35)
                showDtatFrame.place(x=370, y=45)

                labelNom = ct.CTkLabel(showDtatFrame, text="Nom : ", font=("sans serif", 12, "bold"))
                labelNom.grid(row=0, column=0, sticky=W)

                label1 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 12, "bold"))
                label1.grid(row=0, column=1, sticky=W)




                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Prenom from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelPrenom = ct.CTkLabel(showDtatFrame, text="Prénom  : ", font=("sans serif", 12, "bold"))
                labelPrenom.grid(row=1, column=0, sticky=W)

                label2 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 12, "bold"))
                label2.grid(row=1, column=1, sticky=W)








                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Sexe from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelSexe = ct.CTkLabel(showDtatFrame, text="Sexe : ", font=("sans serif", 12, "bold"))
                labelSexe.grid(row=2, column=0, sticky=W)

                label3 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 12, "bold"))
                label3.grid(row=2, column=1, sticky=W)






                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Email from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelEmail = ct.CTkLabel(showDtatFrame, text="Email : ", font=("sans serif", 12, "bold"))
                labelEmail.grid(row=3, column=0, sticky=W)

                label4 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 12, "bold"))
                label4.grid(row=3, column=1, sticky=W)





                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Nationnalité from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelNationnalite = ct.CTkLabel(showDtatFrame, text="Nationnalité : ", font=("sans serif", 10, "bold"))
                labelNationnalite.grid(row=4, column=0, sticky=W)

                label5 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 10, "bold"))
                label5.grid(row=4, column=1, sticky=W)





                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Piece from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelPiece = ct.CTkLabel(showDtatFrame, text="Pièce : ", font=("sans serif", 10, "bold"))
                labelPiece.grid(row=5, column=0, sticky=W)

                label6 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 10, "bold"))
                label6.grid(row=5, column=1, sticky=W)






                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Num_Piece from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelPiece = ct.CTkLabel(showDtatFrame, text="Numéro Pièce : ", font=("sans serif", 10, "bold"))
                labelPiece.grid(row=6, column=0, sticky=W)

                label7 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 10, "bold"))
                label7.grid(row=6, column=1, sticky=W)






                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()
                query = ("select Adresse from client where Contacte=%s")
                value = (self.var_contact.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()


                labelPiece = ct.CTkLabel(showDtatFrame, text="Adresse : ", font=("sans serif", 10, "bold"))
                labelPiece.grid(row=7, column=0, sticky=W)

                label7 = ct.CTkLabel(showDtatFrame, text=row, font=("sans serif", 10, "bold"))
                label7.grid(row=7, column=1, sticky=W)



    def search(self):
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="management"
        )
        mycursor = conn.cursor()

        search_column = self.var_recherche.get()
        search_value = self.txt_recherche.get()

        sql_query = f"SELECT * FROM chambre WHERE {search_column} LIKE '%{search_value}%'"

        mycursor.execute(sql_query)
        rows = mycursor.fetchall()


        if len(rows) != 0:
            self.chambre_Table.delete(*self.chambre_Table.get_children())
            
            for row in rows:
                self.chambre_Table.insert("", END, values=row)
            conn.commit()
        conn.close()

  

    def add_data(self):
        if self.var_contact.get() == "" or self.var_dateArrive.get() == "":
            messagebox.showerror("Error","tous les champs sont obligatoires", parent=self.mac)
        else:
            try:
                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()

                query = """INSERT INTO chambre 
                       (contact, date_arrivee, date_depart, type_chambre, chambre_dispo, repas, nbr_jours) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""

                mycursor.execute(query, (
                    self.var_contact.get(),
                    self.var_dateArrive.get(),
                    self.var_DateDepart.get(),
                    self.var_TypeChambre.get(),
                    self.var_ChambreDispo.get(),
                    self.var_repas.get(),
                    self.var_NbrJours.get()
                ))
                conn.commit()
                self.feech_data()
                conn.close()
                messagebox.showinfo("succes", "La chambre a bien été réservée ✅", parent=self.mac)

            except Exception as es: 
                messagebox.showwarning("avertissement", f"quelque chose s'est mal passé:{(es)}", parent=self.mac)



    def Update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Erreur", "Entrez le contact du client", parent=self.mac)
        else:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="management"
            )
            mycursor = conn.cursor()
            query = """
                UPDATE chambre 
                SET date_arrivee=%s, date_depart=%s, type_chambre=%s, chambre_dispo=%s, 
                    repas=%s, nbr_jours=%s, taxe_paye=%s, sous_total=%s, cout_total=%s 
                WHERE contact=%s
            """
            values = (
                self.var_dateArrive.get(),
                self.var_DateDepart.get(),
                self.var_TypeChambre.get(),
                self.var_ChambreDispo.get(),
                self.var_repas.get(),
                self.var_NbrJours.get(),
                self.var_TaxePaye.get(),
                self.var_SousTotal.get(),
                self.var_coutTotal.get(),
                self.var_contact.get()
            )
            try:
                mycursor.execute(query, values)
                conn.commit()
                self.feech_data()
                conn.close()
                messagebox.showinfo("Update", "Mise à jour réussie ✅", parent=self.mac)
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de la mise à jour : {e}", parent=self.mac)



    def mDelete(self):
        mDelete = messagebox.askyesno("Gestion D'Hotel façon Mister Py", "Voulez vous supprimer ce client?", parent=self.mac)
        if mDelete > 0:
            conn = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="management"
                    )
            mycursor = conn.cursor()
            query = "delete from chambre where contact=%s"
            value = (self.var_contact.get(),)
            mycursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        conn.close()
        self.feech_data()



    def reset(self):
        self.var_contact.set("")
        self.var_dateArrive.set("")
        self.var_DateDepart.set("")
        self.var_TypeChambre.set("")
        self.var_ChambreDispo.set("")
        self.var_repas.set("")
        self.var_NbrJours.set("")
        self.var_TaxePaye.set("")
        self.var_SousTotal.set("")
        self.var_coutTotal.set("")
        


    def feech_data(self):
        conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )
        mycursor = conn.cursor()
        query = "select * from chambre"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.chambre_Table.delete(*self.chambre_Table.get_children())
            for i in rows:
                self.chambre_Table.insert("", END, values=i)
            conn.commit()
        conn.close() 



    def get_cursor(self, event=""):
        cursor_row = self.chambre_Table.focus()
        content = self.chambre_Table.item(cursor_row)
        row = content["values"]


        self.var_contact.set(row[0])
        self.var_dateArrive.set(row[1])
        self.var_DateDepart.set(row[2])
        self.var_TypeChambre.set(row[3])
        self.var_ChambreDispo.set(row[4])
        self.var_repas.set(row[5])
        self.var_NbrJours.set(row[6])
        self.var_TaxePaye.set(row[7])
        self.var_SousTotal.set(row[8])
        self.var_coutTotal.set(row[9])



    def total(self):
        DateArrivee = self.var_dateArrive.get()
        DateDepart = self.var_DateDepart.get()
        DateArrivee = datetime.strptime(DateArrivee,"%d/%m/%Y")
        DateDepart = datetime.strptime(DateDepart, "%d/%m/%Y")
        self.var_NbrJours.set(abs(DateDepart-DateArrivee).days)


        TaxeChambreLuxe = 0.15
        TaxeChambreCelibat = 0.1
        TaxeChambrePourDeux = 0.2

        ChambreLuxe = 35000
        ChambreCelibat = 20000
        ChambrePourDeux = 30000

        PetitDejeuneLuxe = 10000
        PetitDejeuneCelibat = 7000
        PetitDejeunePourDeux = 15000

        DejeuneLuxe = 12000
        DejeuneCelibat = 10000
        DejeunerPourDeux = 15000

        DineLuxe = 12000
        DineCelibat = 8000
        DinePourDeux = 15000

        LesTroisRepasLuxe = 25000
        LesTroisRepasCelibat = 15000
        LesTroisRepasPourDeux = 30000



        

        if (self.var_repas.get()=="Petit Déjeuné" and self.var_TypeChambre.get() =="Luxe"):
            PrixChambre = float(ChambreLuxe)
            PrixRepas = float(PetitDejeuneLuxe)
            PrixNbrJours = float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreLuxe))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreLuxe)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Petit Déjeuné" and self.var_TypeChambre.get() =="Pour deux"):
            PrixChambre = float(ChambrePourDeux)
            PrixRepas = float(PetitDejeunePourDeux)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambrePourDeux))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambrePourDeux)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Petit Déjeuné" and self.var_TypeChambre.get() =="Célibataire"):
            PrixChambre = float(ChambreCelibat)
            PrixRepas = float(PetitDejeuneCelibat)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreCelibat))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreCelibat)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Déjeuné" and self.var_TypeChambre.get() =="Luxe"):
            PrixChambre = float(ChambreLuxe)
            PrixRepas = float(DejeuneLuxe)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreLuxe))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreLuxe)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Déjeuné" and self.var_TypeChambre.get() =="Pour deux"):
            PrixChambre = float(ChambrePourDeux)
            PrixRepas = float(DejeunerPourDeux)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambrePourDeux))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambrePourDeux)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Déjeuné" and self.var_TypeChambre.get() =="Célibataire"):
            PrixChambre = float(ChambreCelibat)
            PrixRepas = float(DejeuneCelibat)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreCelibat))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreCelibat)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Diné" and self.var_TypeChambre.get() =="Luxe"):
            PrixChambre = float(ChambreLuxe)
            PrixRepas = float(DineLuxe)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreLuxe))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreLuxe)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Diné" and self.var_TypeChambre.get() =="Pour deux"):
            PrixChambre = float(ChambrePourDeux)
            PrixRepas = float(DinePourDeux)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambrePourDeux))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambrePourDeux)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Diné" and self.var_TypeChambre.get() =="Célibataire"):
            PrixChambre = float(ChambreCelibat)
            PrixRepas = float(DineCelibat)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreCelibat))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreCelibat)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Les Trois Repas" and self.var_TypeChambre.get()=="Luxe"):
            PrixChambre = float(ChambreLuxe)
            PrixRepas = float(LesTroisRepasLuxe)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreLuxe))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreLuxe)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)
        

        elif (self.var_repas.get()=="Les Trois Repas" and self.var_TypeChambre=="Pour deux"):
            PrixChambre = float(ChambrePourDeux)
            PrixRepas = float(LesTroisRepasPourDeux)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambrePourDeux))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambrePourDeux)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)


        elif (self.var_repas.get()=="Les Trois Repas" and self.var_ChambreDispo=="Célibataire"):
            PrixChambre = float(ChambreCelibat)
            PrixRepas = float(LesTroisRepasCelibat)
            PrixNbrJours= float(self.var_NbrJours.get())
            Somme = float(PrixChambre+PrixRepas)
            CoutT = float(PrixNbrJours+Somme)
            Taxe = str("%.2f"%((CoutT)*TaxeChambreCelibat))+" FCFA"
            St = str("%.2f"%((CoutT)))+" FCFA"
            Tt = str("%.2f"%(CoutT+((CoutT)*TaxeChambreCelibat)))+" FCFA"
            self.var_TaxePaye.set(Taxe)
            self.var_SousTotal.set(St)
            self.var_coutTotal.set(Tt)















if __name__ == "__main__":
    Mac = ct.CTk()
    obj = chambre_fenetre(Mac)
    Mac.mainloop()