from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ct
from tkinter import ttk
import pymysql
from tkinter import messagebox





class Detail_fenetre:


    def __init__(self,mac):
        self.mac = mac
        self.mac.title("Gestion D'Hotel façon Mister Py 🐍")
        self.mac.geometry("1100x500+245+200")
        self.mac.resizable(0,0)


        self.var_Etage = StringVar()
        self.var_ChambreNum = StringVar()
        self.var_TypeDeChambre = StringVar()


        # ===========================Label Titre=====================
        labelTitle = Label(self.mac, text="RESERVATION DE CHAMBRE", font=('sans serif', 18, 'bold'), bg="black", fg="white", bd=4, relief=RIDGE)
        labelTitle.place(x=0, y=0,  width=1100, height=40)


        # ==============================Image Logo=========================
        img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        img2 = img2.resize((40, 30))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimage = Label(self.mac, image=self.photoimg2, bd=0, relief="ridge")
        labelimage.place(x=5, y=5, width=40, height=30)

        # =======================Label Frame===========
        labelFrameLeft = LabelFrame(self.mac, text="AJOUTER NOUVELLE CHAMBRE",bd=2, relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        labelFrameLeft.place(x=5, y=60, width=420, height=350)


        # ====================== Floor (Étage) ============

        label_Floor = ct.CTkLabel(labelFrameLeft, text="Etage ", font=("sans serif", 15, 'bold'))
        label_Floor.grid(row=0, column=0, pady=5, sticky=W)
    
        entry_Floor = ct.CTkEntry(labelFrameLeft, width=150, textvariable= self.var_Etage, font=("sans serif", 15, 'bold'), placeholder_text="Etage")
        entry_Floor.grid(row=0, column=1, padx= 5, pady=5, sticky=W)




        #============================= Chambre Nº====================
        label_chambre_dispo = ct.CTkLabel(labelFrameLeft, text="Chambre Nº ", font=("sans serif", 15, 'bold'))
        label_chambre_dispo.grid(row=2, column=0, pady=5, sticky=W)
        entry_chambre_dispo = ct.CTkEntry(labelFrameLeft, width=200, textvariable=self.var_ChambreNum,font=("sans serif", 15, 'bold'), placeholder_text="Chambre Nº")
        entry_chambre_dispo.grid(row=2, column=1, padx= 5, pady=5, sticky=W)



        # ====================chambre====================
        label_type_chambre = ct.CTkLabel(labelFrameLeft, text="Type de chambre ", font=("sans serif", 15, 'bold'))
        label_type_chambre.grid(row=3, column=0)
        option_type_chambre = ct.CTkOptionMenu(labelFrameLeft,width=200, variable=self.var_TypeDeChambre,
                                                                      values=["Célibataire", "Pour deux", "Luxe"], state="readonly")
        option_type_chambre.set("Pour deux")
        option_type_chambre.grid(row=3, column=1, padx= 5, pady=5, sticky=W)



        # Buttons
        btn_frame = ct.CTkFrame(labelFrameLeft, corner_radius=20, width=380, height=45)
        btn_frame.place(x=35, y=240)

        btn_Ajout = ct.CTkButton(btn_frame, text="Ajouter", command=self.add_data,
                                                   font=("sans serif", 10, 'bold'), text_color="white", 
                                            fg_color="black" , cursor="hand1",corner_radius=20, width=5)
        btn_Ajout.grid(row=0, column=0, padx=5, pady=6)
        
        btn_MAJ = ct.CTkButton(btn_frame, text="Update",command=self.Update,
                                          font=("sans serif", 10, 'bold'), text_color="white",
                                          fg_color="black" ,cursor="hand1", corner_radius=20, width=5)
        btn_MAJ.grid(row=0, column=1,  padx=5, pady=6)

        btn_Suppr = ct.CTkButton(btn_frame, text="Effacer", command=self.mDelete,
                                                font=("sans serif", 10, 'bold'), text_color="white", 
                                                fg_color="black" ,cursor="hand1",corner_radius=20, width=5)
        btn_Suppr.grid(row=0, column=2, padx=5, pady=6)

        btn_Reset = ct.CTkButton(btn_frame, text="Reset", command=self.reset,
                                                         font=("sans serif", 10, 'bold'), text_color="white",
                                                          fg_color="black" , cursor="hand1", corner_radius=20, width=5)
        btn_Reset.grid(row=0, column=3,  padx=5, pady=6)



        # ====================Table Frame====================
        Table_frame = LabelFrame(self.mac, text="Détails des chambres",bd=2, 
                                           relief=RIDGE, padx=2, font=('sans serif', 18, 'bold'))
        Table_frame.place(x=500, y=60, width=400, height=350)


        Scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        Scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.chambre_Table = ttk.Treeview(Table_frame, column=("Etage", "ChambreNum", "TypeDeChambre"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.chambre_Table.xview)
        Scroll_y.config(command=self.chambre_Table.yview)


        self.chambre_Table.heading("Etage", text="Etage")
        self.chambre_Table.heading("ChambreNum", text="Chambre Nº")
        self.chambre_Table.heading("TypeDeChambre", text="TypeDeChambre")
        self.chambre_Table["show"]="headings"
        


        self.chambre_Table.column("Etage", width=100)
        self.chambre_Table.column("ChambreNum", width=100)
        self.chambre_Table.column("TypeDeChambre", width=100)

        self.chambre_Table.pack(fill=BOTH, expand=1)
        self.chambre_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.feech_data()


    def add_data(self):
        if self.var_Etage.get() == "" or self.var_ChambreNum.get() == "":
            messagebox.showerror("Error","Remplissez les champs svp", parent=self.mac)
        else:
            try:
                conn = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database= "management"
                )
                mycursor = conn.cursor()

                query = """INSERT INTO detail 
                       (Etage, ChambreNum, TypeDeChambre) 
                       VALUES (%s, %s, %s)"""
                
                
                values = ( self.var_Etage.get(),
                    self.var_ChambreNum.get(),
                    self.var_TypeDeChambre.get())

                mycursor.execute(query, values)
                conn.commit()
                self.feech_data()
                conn.close()
                messagebox.showinfo("succes", "La chambre ajoutée avec succès ✅", parent=self.mac)

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
        query = "select * from detail"
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


        self.var_Etage.set(row[0])
        self.var_ChambreNum.set(row[1])
        self.var_TypeDeChambre.set(row[2])



    def Update(self):
        if self.var_Etage.get() == "":
            messagebox.showerror("Erreur", "Entre l'Etage svp", parent=self.mac)
        else:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="management"
            )
            mycursor = conn.cursor()
            query = """
                UPDATE detail 
                SET ChambreNum=%s, TypeDeChambre=%s 
                WHERE Etage=%s
            """
            values = (
                self.var_ChambreNum.get(),
                self.var_TypeDeChambre.get(),
                self.var_Etage.get()
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
            if mDelete>0:
                conn = pymysql.connect(
                            host="localhost",
                            user="root",
                            password="",
                            database="management"
                        )
                mycursor = conn.cursor()
                query = "delete from detail where Etage=%s"
                value = (self.var_Etage.get(),)
            else:
                if not mDelete:
                    return
            mycursor.execute(query, value)
            conn.commit()
            self.feech_data()
            conn.close()



    def reset(self):
            self.var_Etage.set("")
            self.var_ChambreNum.set("")
            self.var_TypeDeChambre.set("Pour deux")






if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Detail_fenetre(Mac)
    Mac.mainloop()