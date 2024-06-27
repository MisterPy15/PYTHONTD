from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3





ct.set_appearance_mode("System")
ct.set_default_color_theme("green")


class cour:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Système de Gestion des Etudiants UTA")
        self.mac.geometry("1200x535+80+170")


        # ===================Titre==================
        title = ct.CTkLabel(self.mac, text="Détails Et Gestion Des Cours", height=35, width=1180, 
                                      padx=10,  compound=LEFT,font=("goudy old style",20, "bold"),
                                      bg_color="#033054", fg_color="green")
        title.place(x=10, y=15)

        # frame_content = ct.CTkFrame(self.mac, width=110, height=500, bg_color="white")
        # frame_content.place(x=50, y=70)




        # ==========================Widgets======================
        label_name_Course = ct.CTkLabel(self.mac, text="Nom du Cour", font=("sans serif", 15, "bold"))
        label_name_Course.place(x=10, y=60)

        label_Duree = ct.CTkLabel(self.mac, text="Durée", font=("sans serif", 15, "bold"))
        label_Duree.place(x=10, y=100)

        label_Charges = ct.CTkLabel(self.mac, text="Charges", font=("sans serif", 15, "bold"))
        label_Charges.place(x=10, y=140)

        label_description = ct.CTkLabel(self.mac, text="Description", font=("sans serif", 15, "bold"))
        label_description.place(x=10, y=180)


        # ===============================Variables===============================
        self.var_Cours = StringVar()
        self.var_Duree = StringVar()
        self.var_Charge = StringVar()
        self.var_recherche = StringVar()


        # ================================Entry===================================
        self.txt_name_Course = ct.CTkEntry(self.mac, placeholder_text="Nom du cour", textvariable=self.var_Cours, font=("sans serif", 15, "bold"), width=200)
        self.txt_name_Course.place(x=150, y=60)

        txt_Duree = ct.CTkEntry(self.mac, placeholder_text="Entrez la durée", textvariable=self.var_Duree, font=("sans serif", 15, "bold"), width=200)
        txt_Duree.place(x=150, y=100)

        txt_Charges = ct.CTkEntry(self.mac, placeholder_text="Entrez les charges", textvariable=self.var_Charge, font=("sans serif", 15, "bold"), width=200)
        txt_Charges.place(x=150, y=140)

        self.txt_description = Text(self.mac, font=("sans serif", 15, "bold"))
        self.txt_description.place(x=150, y=180, width=500, height=100)


        # ======================================Buttons==============================
        self.buttonAjout = ct.CTkButton(self.mac, text="Enregister", text_color="white", font=("sans serif", 12, "bold"), fg_color="green", command=self.add,
                                                  corner_radius=20, width=110)
        self.buttonAjout.place(x=150, y=400)

        self.buttonMAJ = ct.CTkButton(self.mac, text="Mise à jour",text_color="green", font=("sans serif", 12, "bold"),fg_color="white", command=self.Update,
                                                  corner_radius=20, width=110)
        self.buttonMAJ.place(x=270, y=400)

        self.buttonSuppr = ct.CTkButton(self.mac, text="Supprimer",text_color="white", font=("sans serif", 12, "bold"),fg_color="green", command=self.Delete,
                                                  corner_radius=20, width=110)
        self.buttonSuppr.place(x=390, y=400)

        self.buttonEffacer = ct.CTkButton(self.mac, text="Effacer", text_color="green",font=("sans serif", 12, "bold"),fg_color="white", command=self.clear,
                                                    corner_radius=20, width=110)
        self.buttonEffacer.place(x=510, y=400)


      # =========================Recherche=======================
        label_recherche = ct.CTkLabel(self.mac, text="Nom du cour", font=("sans serif", 15, "bold"))
        label_recherche.place(x=720, y=60)

        entry_recherche = ct.CTkEntry(self.mac, font=("sans serif", 15, "bold"), textvariable=self.var_recherche, width=200)
        entry_recherche.place(x=830, y=60)
        

        buttonSearch = ct.CTkButton(self.mac, text="Rechercher", text_color="white",font=("sans serif", 12, "bold"),fg_color="green", command=self.search,
                                                    corner_radius=20, width=110)
        buttonSearch.place(x=1050, y=60)


        self.C_Frame = Frame(self.mac, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        Scroll_y = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scroll_x = Scrollbar(self.C_Frame, orient=HORIZONTAL)


        self.CourseTable = ttk.Treeview(self.C_Frame, column=("cid", "nom", "Durée", "Charge","Description"),
                                                      xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.CourseTable.xview)
        Scroll_y.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Id Cours")
        self.CourseTable.heading("nom", text="Nom")
        self.CourseTable.heading("Durée", text="Durée")
        self.CourseTable.heading("Charge", text="Charge")
        self.CourseTable.heading("Description", text="Description")
        
        self.CourseTable["show"]="headings"
        
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("nom", width=100)
        self.CourseTable.column("Durée", width=100)
        self.CourseTable.column("Charge", width=100)
        self.CourseTable.column("Description", width=150)
       
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def get_data(self, ev):
      # self.txt_name_Course.configure(state="readonly")
      r = self.CourseTable.focus()
      content = self.CourseTable.item(r)
      row = content["values"]
      

      self.var_Cours.set(row[1])
      self.var_Duree.set(row[2])
      self.var_Charge.set(row[3])
      self.txt_description.delete('1.0', END)
      self.txt_description.insert(END, row[4])





    def add(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            if self.var_Cours.get()=="" or self.var_Duree.get()=="":
              messagebox.showerror("Erreur", "Entrez le nom du Cour.", parent=self.mac)
            else:
              query = "select * from Cours where nom=?"
              cur.execute(query, (self.var_Cours.get(),))
              row=cur.fetchone()
              if row !=None:
                messagebox.showerror("Erreur", "Le cour saisi est existe déja", parent=self.mac)
              else:

                query = "insert into Cours (nom, Durée, Charge, Description) values(?, ?, ?, ?)"
                values = (self.var_Cours.get(), 
                          self.var_Duree.get(), 
                          self.var_Charge.get(), 
                          self.txt_description.get("1.0", END))
                cur.execute(query, values)
                conn.commit()
                messagebox.showinfo("succes", "Cours Ajouter avec Succès", parent=self.mac)
                self.show()
          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)


    def show(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            query = "select * from Cours" 
            cur.execute(query)
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
              self.CourseTable.insert('', END,values=row)

          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)


    def Update(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            if self.var_Cours.get()=="":
              messagebox.showerror("Erreur", "Le nom du cour est Obligatoire", parent=self.mac)
            else:
              query = "select * from Cours where nom=?"
              cur.execute(query, (self.var_Cours.get(),))
              row=cur.fetchone()
              if row == None:
                messagebox.showerror("Erreur", "Sélecctionnez un cour dans la liste", parent=self.mac)
              else:

                query = "update Cours set Durée=?,  Charge=?, Description=? where nom=?"
                values = (self.var_Duree.get(), 
                          self.var_Charge.get(), 
                          self.txt_description.get("1.0", "end-1c"),
                          self.var_Cours.get())
                cur.execute(query, values)
                conn.commit()
                messagebox.showinfo("succes", "Mise a jour réussie", parent=self.mac)
                self.show()
          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)



    def Delete(self):
        conn = sqlite3.connect(database="school_managment.db")
        cur = conn.cursor()

        try:
            if self.var_Cours.get()=="" or self.var_Duree.get()=="":
              messagebox.showerror("Erreur", "Entrez le nom du Cour.", parent=self.mac)
            else:
              query = "select * from Cours where nom=?"
              cur.execute(query, (self.var_Cours.get(),))
              row=cur.fetchone()
              if row ==None:
                messagebox.showerror("Erreur", "svp sélectionnez un cour dans la liste", parent=self.mac)
              else:
                op = messagebox.askyesno("Attention", "voulez Vraiment Supprimer ?", parent=self.mac)
                if op == True:
                  query = "delete from Cours where nom=?"
                  value = (self.var_Cours.get(),)
                  cur.execute(query, value)
                  conn.commit()
                  messagebox.showinfo("Succès", "Cour supprimr avec succès")
                  self.clear()
                  self.show()
        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)



    def clear(self):
      self.show()    
      self.var_Cours.set("")
      self.var_Duree.set("")
      self.var_Charge.set("")
      self.txt_description.delete("1.0", "end")
      self.txt_description.insert("1.0", "")
      self.var_recherche.set("")
      
      

    def search(self):
      conn = sqlite3.connect(database="school_managment.db")
      cur = conn.cursor()

      try:
          query = "SELECT * FROM Cours WHERE nom LIKE ?"
          search_term = '%' + self.var_recherche.get() + '%'
          cur.execute(query, (search_term,))
          rows = cur.fetchall()
          self.CourseTable.delete(*self.CourseTable.get_children())

          for row in rows:
              self.CourseTable.insert('', END, values=row)

      except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur due à {str(ex)}", parent=self.mac)








if __name__ == "__main__":
    Mac = ct.CTk()
    obj = cour(Mac)
    Mac.mainloop()