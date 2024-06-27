from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ct
from tkinter import ttk
import random as rd
import pymysql
from tkinter import messagebox



ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

class Client_fenetre:
    

    def __init__(self,mac):
        self.mac = mac
        self.mac.title("Gestion D'Hotel façon Mister Py 🐍")
        self.mac.geometry("1100x540+245+180")
        self.mac.resizable(0,0)


        # =============Variables=====================
        self.var_ref = StringVar()
        x = rd.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_nom_client = StringVar()
        self.var_prenom_client = StringVar()
        self.var_sexe = StringVar()
        self.var_contacte = StringVar()
        self.var_email = StringVar()
        self.var_nationnalite = StringVar()
        self.var_piece = StringVar()
        self.var_num_piece = StringVar()
        self.var_adresse = StringVar()

        # ===========================Label Titre=====================
        labelTitle = Label(self.mac, text="DETAILS CLIENTS", font=('sans serif', 18, 'bold'), bg="black", fg="white", bd=4, relief=RIDGE)
        labelTitle.place(x=0, y=0, width=1100, height=40)


        # ==============================Image Logo=========================
        img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        img2 = img2.resize((40, 30))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimage = Label(self.mac, image=self.photoimg2, bd=0, relief="ridge")
        labelimage.place(x=5, y=5, width=40, height=30)


        # =======================Label Frame===========
        labelFrameLeft = LabelFrame(self.mac, text="Détails Clients",bd=2, relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        labelFrameLeft.place(x=5, y=40, width=330, height=450)


        # ====================== Info Clients============

        label_CLient_Ref = Label(labelFrameLeft, text="Ref client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Ref.grid(row=0, column=0)
        entry_Client_Ref = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_ref, font=("sans serif", 12, 'bold'), state="readonly")
        entry_Client_Ref.grid(row=0, column=1, sticky=W)



        label_CLient_Nom = Label(labelFrameLeft, text="Nom client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Nom.grid(row=1, column=0)
        entry_Client_Nom = ct.CTkEntry(labelFrameLeft, width=200,textvariable=self.var_nom_client, font=("sans serif", 12, 'bold'))
        entry_Client_Nom.grid(row=1, column=1, sticky=W)



        label_CLient_Prenom = Label(labelFrameLeft, text="Prenom client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Prenom.grid(row=2, column=0)
        entry_Client_Prenom = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_prenom_client, font=("sans serif", 12, 'bold'))
        entry_Client_Prenom.grid(row=2, column=1, sticky=W)



        label_CLient_Sexe = Label(labelFrameLeft, text="Sexe", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Sexe.grid(row=3, column=0)

        option_Sexe = ct.CTkOptionMenu(labelFrameLeft,width=200, variable=self.var_sexe,
                                                       values=["Homme", "Femme", "Autre"])
        option_Sexe.set("Homme")
        option_Sexe.grid(row=3, column=1, sticky=W)

      
       



        label_CLient_Contacte = Label(labelFrameLeft, text="Contacte client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Contacte.grid(row=4, column=0)
        entry_Client_Contacte = ct.CTkEntry(labelFrameLeft,width=200, textvariable= self.var_contacte,font=("sans serif", 12, 'bold'))
        entry_Client_Contacte.grid(row=4, column=1, sticky=W)


        label_CLient_Email = Label(labelFrameLeft, text="Email client", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Email.grid(row=5, column=0)
        entry_Client_Email = ct.CTkEntry(labelFrameLeft,width=200, textvariable=self.var_email, font=("sans serif", 12, 'bold'))
        entry_Client_Email.grid(row=5, column=1, sticky=W)



        label_CLient_Nationnalite = Label(labelFrameLeft, text="Nationnalité", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Nationnalite.grid(row=6, column=0)

        option_CLient_Nationnalite = ct.CTkOptionMenu(labelFrameLeft,width=200, variable=self.var_nationnalite, 
                                                                      values=["Ivoirien", "Américain", "Français","Ghanéen"])
        option_CLient_Nationnalite.set("Ivoirien")
        option_CLient_Nationnalite.grid(row=6, column=1, sticky=W)


    

        label_CLient_Piece = Label(labelFrameLeft, text="Pièce", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Piece.grid(row=7, column=0)

        option_CLient_Piece = ct.CTkOptionMenu(labelFrameLeft, width=200, variable=self.var_piece, 
                                                                values=["CNI", "PASSEPORT", "PERMIS DE CONDUIRE"])
        option_CLient_Piece.set("CNI")
        option_CLient_Piece.grid(row=7, column=1, sticky=W)

       


        label_CLient_PieceID = Label(labelFrameLeft, text="Nº Piece ID", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_PieceID.grid(row=8, column=0)
        entry_Client_PieceID = ct.CTkEntry(labelFrameLeft, width=200,textvariable=self.var_num_piece, font=("sans serif", 12,'bold'))
        entry_Client_PieceID.grid(row=8, column=1, sticky=W)



        label_CLient_Adresse = Label(labelFrameLeft, text="Adresse", font=("sans serif", 12, 'bold'), padx=2, pady=6)
        label_CLient_Adresse.grid(row=9, column=0)
        entry_Client_Adresse = ct.CTkEntry(labelFrameLeft,width=200, textvariable=self.var_adresse, font=("sans serif", 12, 'bold'))
        entry_Client_Adresse.grid(row=9, column=1, sticky=W)
        




        # ===============================btns=================================

        btn_frame = Frame(labelFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=20, y=370, width=300, height=45)

        btn_Ajout = ct.CTkButton(btn_frame, text="Ajouter", command=self.add_data, 
                                            font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" , cursor="hand1",corner_radius=20, width=5)
        btn_Ajout.grid(row=0, column=0, padx=4, pady=6)
        
        btn_MAJ = ct.CTkButton(btn_frame, text="Update", command=self.Update,
                                          font=("sans serif", 10, 'bold'), text_color="white",
                                          fg_color="black" ,cursor="hand1", corner_radius=20, width=5)
        btn_MAJ.grid(row=0, column=1,  padx=4, pady=6)

        btn_Suppr = ct.CTkButton(btn_frame, text="Effacer", command=self.mDelete,
                                            font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" ,cursor="hand1",corner_radius=20, width=5)
        btn_Suppr.grid(row=0, column=2, padx=4, pady=6)

        btn_Reset = ct.CTkButton(btn_frame, text="Reset", command=self.reset,
                                            font=("sans serif", 10, 'bold'), text_color="white", fg_color="black" , cursor="hand1", corner_radius=20, width=5)
        btn_Reset.grid(row=0, column=3,  padx=4, pady=6)



        # ====================Table Frame====================
        Table_frame = LabelFrame(self.mac, text="Vues des détails et Système de Recherche",bd=2, 
                                           relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        Table_frame.place(x=380, y=40, width=690, height=480)



        label_recherche = Label(Table_frame, text="Rechercher par: ",
                                             font=("sans serif", 12, 'bold'), bg="red", fg="#fff")
        label_recherche.grid(row=0, column=0, padx=2)



        self.var_recherche = StringVar()
        option_Recherche = ct.CTkOptionMenu(Table_frame, variable = self.var_recherche, values=["Contacte", "Ref"])
        option_Recherche.set("Contacte")
        option_Recherche.grid(row=0, column=1, pady=0)



        self.txt_recherche = StringVar()
        entry_Recherche = ct.CTkEntry(Table_frame, textvariable = self.txt_recherche, font=("sans serif", 12, 'bold'))
        entry_Recherche.grid(row=0, column=2, padx=2, sticky=W)


        btn_Search =  ct.CTkButton(Table_frame, text="Search", command= self.search,
                                                font=("sans serif", 10, 'bold'), text_color="white",
                                                fg_color="black" , cursor="hand1", corner_radius=20, width=10)
        btn_Search.grid(row=0, column=3, padx=1)
        
        btn_Show_All = ct.CTkButton(Table_frame, text="Show All", command=self.feech_data,
                                                 font=("sans serif", 10, 'bold'), text_color="white", fg_color="black" , cursor="hand1", corner_radius=20, width=10)
        btn_Show_All.grid(row=0, column=4, padx=1)




        # ============================Show Data Table==================
        details_table = Frame(Table_frame, bd=2, relief=RIDGE, bg="black")
        details_table.place(x=0, y=50, width=685, height=405)

        Scroll_x = Scrollbar(details_table, orient=HORIZONTAL)
        Scroll_y = Scrollbar(details_table, orient=VERTICAL)


        self.client_detail_Table = ttk.Treeview(details_table, column=("Ref", "Nom", "Prenom", "Sexe", "Contacte",
                                                                        "Email", "Nationnalité", "Piece", "Num_Piece", 
                                                                        "Adresse"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.client_detail_Table.xview)
        Scroll_y.config(command=self.client_detail_Table.yview)

        self.client_detail_Table.heading("Ref", text="Ref Nº")
        self.client_detail_Table.heading("Nom", text="Nom")
        self.client_detail_Table.heading("Prenom", text="Prenom")
        self.client_detail_Table.heading("Sexe", text="Sexe")
        self.client_detail_Table.heading("Contacte", text="Contacte")
        self.client_detail_Table.heading("Email", text="Email")
        self.client_detail_Table.heading("Nationnalité", text="Nationnalité")
        self.client_detail_Table.heading("Piece", text="Piece")
        self.client_detail_Table.heading("Num_Piece", text="Nº Piece")
        self.client_detail_Table.heading("Adresse", text="Adresse")

        self.client_detail_Table["show"]="headings"
        

        self.client_detail_Table.column("Ref", width=100)
        self.client_detail_Table.column("Nom", width=100)
        self.client_detail_Table.column("Prenom", width=100)
        self.client_detail_Table.column("Sexe", width=100)
        self.client_detail_Table.column("Contacte", width=100)
        self.client_detail_Table.column("Email", width=200)
        self.client_detail_Table.column("Nationnalité", width=100)
        self.client_detail_Table.column("Piece", width=100)
        self.client_detail_Table.column("Num_Piece", width=100)
        self.client_detail_Table.column("Adresse", width=100)


        self.client_detail_Table.pack(fill=BOTH, expand=1)
        self.client_detail_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.feech_data()



    def add_data(self):
        if self.var_contacte.get() == "" or self.var_prenom_client.get() == "":
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
                mycursor.execute("insert into client values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                (self.var_ref.get(),
                                                                                self.var_nom_client.get(),
                                                                                self.var_prenom_client.get(),
                                                                                self.var_sexe.get(),
                                                                                self.var_contacte.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationnalite.get(),
                                                                                self.var_piece.get(),
                                                                                self.var_num_piece.get(),
                                                                                self.var_adresse.get()
                                                                                
                                                                                ))
                conn.commit()
                self.feech_data()
                conn.close()
                messagebox.showinfo("succes", "Le clients a bien été Ajouter", parent=self.mac)

            except Exception as es: 
                messagebox.showwarning("avertissement", f"quelque chose s'est mal passé:{(es)}", parent=self.mac)


    def feech_data(self):
        conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
        mycursor = conn.cursor()
        mycursor.execute("select * from client")
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.client_detail_Table.delete(*self.client_detail_Table.get_children())
            for i in rows:
                self.client_detail_Table.insert("", END, values=i)
            conn.commit()
        conn.close() 



    def get_cursor(self, event=""):
        cursor_row = self.client_detail_Table.focus()
        content = self.client_detail_Table.item(cursor_row)
        row = content["values"]


        self.var_ref.set(row[0])
        self.var_nom_client.set(row[1])
        self.var_prenom_client.set(row[2])
        self.var_sexe.set(row[3])
        self.var_contacte.set(row[4])
        self.var_email.set(row[5])
        self.var_nationnalite.set(row[6])
        self.var_piece.set(row[7])
        self.var_num_piece.set(row[8])
        self.var_adresse.set(row[9])



    def Update(self):

        if self.var_contacte == "":
            messagebox.showerror("Erreur", "Entrez le contacte du client", parent=self.mac)

        else:
            conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )
            mycursor = conn.cursor()
            mycursor.execute("update client set Nom=%s, Prenom=%s, Sexe=%s, Contacte=%s, Email=%s, Nationnalité=%s, Piece=%s, Num_Piece=%s, Adresse=%s where Ref=%s",(
                                                                                                                                        
                                                                                                                                        self.var_nom_client.get(),
                                                                                                                                        self.var_prenom_client.get(),
                                                                                                                                        self.var_sexe.get(),
                                                                                                                                        self.var_contacte.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_nationnalite.get(),
                                                                                                                                        self.var_piece.get(),
                                                                                                                                        self.var_num_piece.get(),
                                                                                                                                        self.var_adresse.get(),
                                                                                                                                        self.var_ref.get()
                                                                                                                                        ))
            conn.commit()
            self.feech_data()
            conn.close()
            messagebox.showinfo("Update", "Succès de la mise à jour des Détails du client", parent=self.mac)


    def mDelete(self):
        mDelete = messagebox.askyesno("Gestion D'Hotel façon Mister Py", "Voulez vous supprimer ce client?", parent=self.mac)
        if mDelete>0:
            conn = pymysql.connect(
                        host = "localhost",
                        user = "root",
                        password = "",
                        database= "management"
                    )
            mycursor = conn.cursor()
            query = "delete from client where Ref=%s"
            value = (self.var_ref.get(),)
            mycursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.feech_data()
        conn.close()



    def reset(self):
        # self.var_ref.set("")
        self.var_nom_client.set("")
        self.var_prenom_client.set("")
        # self.var_sexe.set("")
        self.var_contacte.set("")
        self.var_email.set("")
        # self.var_nationnalite.set("")
        # self.var_piece.set("")
        self.var_num_piece.set("")
        self.var_adresse.set("")
        
        x = rd.randint(1000, 9999)
        self.var_ref.set(str(x))




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

        sql_query = f"SELECT * FROM client WHERE {search_column} LIKE '%{search_value}%'"

        mycursor.execute(sql_query)
        rows = mycursor.fetchall()

        if len(rows) != 0:
            self.client_detail_Table.delete(*self.client_detail_Table.get_children())

            for row in rows:
                self.client_detail_Table.insert("", END, values=row)
            
            conn.commit()
        conn.close()






























if __name__ == "__main__":
    Mac = ct.CTk()
    Obj = Client_fenetre(Mac)
    Mac.mainloop()
