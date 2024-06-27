from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import random as rd




ct.set_appearance_mode("System")
ct.set_default_color_theme("green")



class Etudiants:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Système de Gestion des Etudiants UTA")
        self.mac.geometry("1200x535+80+170")

       
        # ===================Titre==================
        title = ct.CTkLabel(self.mac, text="Détails Et Gestion Des Etudiants", height=35, width=590, 
                                      padx=10,  compound=LEFT,font=("goudy old style",20, "bold"),
                                      bg_color="#033054", fg_color="green")
        title.place(x=10, y=15)

        # ===============================Variables===============================
        self.var_matricule = StringVar()
        self.var_Nom = StringVar()
        self.var_Prenom = StringVar()
        self.var_Email = StringVar()
        self.var_sexe = StringVar()
        self.var_Niveau = StringVar()
        self.var_DateNaiss = StringVar()
        self.var_Contact = StringVar()
        self.var_CoursSelect = StringVar()
        self.var_Date_Admission = StringVar()
        self.var_Ville = StringVar()
        self.var_Pin = StringVar()
        x = rd.randint(1000, 9999)
        self.var_Pin.set(str(x))



        # frame_content = ct.CTkFrame(self.mac, width=110, height=500, bg_color="white")
        # frame_content.place(x=50, y=70)




        # ==========================Label Column1======================
        label_NumMat = ct.CTkLabel(self.mac, text="Nº Matricule", font=("sans serif", 15, "bold"))
        label_NumMat.place(x=10, y=60)

        label_Nom = ct.CTkLabel(self.mac, text="Nom", font=("sans serif", 15, "bold"))
        label_Nom.place(x=10, y=100)

        label_Prenom = ct.CTkLabel(self.mac, text="Prenom", font=("sans serif", 15, "bold"))
        label_Prenom.place(x=10, y=140)

        label_Email = ct.CTkLabel(self.mac, text="Email", font=("sans serif", 15, "bold"))
        label_Email.place(x=10, y=180)

        label_Sexe = ct.CTkLabel(self.mac, text="Sexe", font=("sans serif", 15, "bold"))
        label_Sexe.place(x=10, y=220)

        label_Niveau = ct.CTkLabel(self.mac, text="Niveau", font=("sans serif", 15, "bold"))
        label_Niveau.place(x=10, y=260)

        label_Adresse = ct.CTkLabel(self.mac, text="Adresse", font=("sans serif", 15, "bold"))
        label_Adresse.place(x=10, y=320)



        # ================================Entry column1===================================
        self.txt_NumMat= ct.CTkEntry(self.mac, placeholder_text="Nº Matricule", textvariable=self.var_matricule, font=("sans serif", 15, "bold"), width=150)
        self.txt_NumMat.place(x=150, y=60)

        txt_Nom = ct.CTkEntry(self.mac, placeholder_text="Entrez la durée", textvariable=self.var_Nom, font=("sans serif", 15, "bold"), width=150)
        txt_Nom.place(x=150, y=100)

        txt_Prenom = ct.CTkEntry(self.mac, placeholder_text="Entrez les charges", textvariable=self.var_Prenom, font=("sans serif", 15, "bold"), width=150)
        txt_Prenom.place(x=150, y=140)

        txt_Email = ct.CTkEntry(self.mac, placeholder_text="Entrez la durée", textvariable=self.var_Email, font=("sans serif", 13, "bold"), width=150)
        txt_Email.place(x=150, y=180)

        self.option_Sexe = ct.CTkOptionMenu(self.mac, values=["Masculin", "Féminin", "Autre"], variable=self.var_sexe, state="readonly", width=150)
        self.option_Sexe.set("Masculin")
        self.option_Sexe.place(x=150, y=220)


        self.option_Niveau = ct.CTkOptionMenu(self.mac, values=["Licence 1", "Licence 2", "Licence 3", "BTS 1", "BTS 2", "Master 1", "Master 2"], width=150, variable=self.var_Niveau, state="readonly")
        self.option_Niveau.set("Licence/BTS/Master")
        self.option_Niveau.place(x=150, y=260)

        self.txt_Adresse = Text(self.mac, font=("sans serif", 15, "bold"))
        self.txt_Adresse.place(x=150, y=320, width=450, height=100)



        # ==========================Label Column2======================
        label_DateNaiss = ct.CTkLabel(self.mac, text="Né(e) le", font=("sans serif", 15, "bold"))
        label_DateNaiss.place(x=330, y=60)

        label_Contacte = ct.CTkLabel(self.mac, text="Contacte", font=("sans serif", 15, "bold"))
        label_Contacte.place(x=330, y=100)

        label_selectCourse = ct.CTkLabel(self.mac, text="Cours", font=("sans serif", 15, "bold"))
        label_selectCourse.place(x=330, y=140)

        label_DateAdmission = ct.CTkLabel(self.mac, text="Date Admission", font=("sans serif", 15, "bold"))
        label_DateAdmission.place(x=330, y=180)

        label_Ville = ct.CTkLabel(self.mac, text="Ville", font=("sans serif", 15, "bold"))
        label_Ville.place(x=330, y=220)

        label_PinCode = ct.CTkLabel(self.mac, text="Ref", font=("sans serif", 15, "bold"))
        label_PinCode.place(x=330, y=260)





        # ================================Entry column2===================================
        self.DateNaiss= ct.CTkEntry(self.mac, textvariable=self.var_DateNaiss, font=("sans serif", 15, "bold"), width=150)
        self.DateNaiss.place(x=450, y=60)

        txt_Contacte = ct.CTkEntry(self.mac, textvariable=self.var_Contact, font=("sans serif", 15, "bold"), width=150)
        txt_Contacte.place(x=450, y=100)


        
        conn = sqlite3.connect(database="school_managment.db")
        cur = conn.cursor()
        query = "select nom from Cours"
        cur.execute(query)
        rows = cur.fetchall()


        OptionCoursSelect = ct.CTkOptionMenu(self.mac, values=[row[0] for row in rows], variable=self.var_CoursSelect)
        OptionCoursSelect.set("Cours")
        OptionCoursSelect.place(x=450, y=140)

        
        txt_DateAdmission = ct.CTkEntry(self.mac, textvariable=self.var_Date_Admission, font=("sans serif", 15, "bold"), width=150)
        txt_DateAdmission.place(x=450, y=180)

        txt_Ville = ct.CTkEntry(self.mac, textvariable=self.var_Ville, font=("sans serif", 15, "bold"), width=150)
        txt_Ville.place(x=450, y=220)

        txt_PinCode = ct.CTkEntry(self.mac, textvariable=self.var_Pin, font=("sans serif", 15, "bold"), width=150, state="readonly")
        txt_PinCode.place(x=450, y=260)




        # ======================================Buttons==============================
        self.buttonAjout = ct.CTkButton(self.mac, text="Enregister", text_color="white", font=("sans serif", 12, "bold"), fg_color="green", command=self.add,
                                                  corner_radius=20, width=110)
        self.buttonAjout.place(x=120, y=450)

        self.buttonMAJ = ct.CTkButton(self.mac, text="Mise à jour",text_color="green", font=("sans serif", 12, "bold"),fg_color="white", command=self.Update,
                                                  corner_radius=20, width=110)
        self.buttonMAJ.place(x=240, y=450)

        self.buttonSuppr = ct.CTkButton(self.mac, text="Supprimer",text_color="white", font=("sans serif", 12, "bold"),fg_color="green", command=self.Delete,
                                                  corner_radius=20, width=110)
        self.buttonSuppr.place(x=360, y=450)

        self.buttonEffacer = ct.CTkButton(self.mac, text="Réinitialiser", text_color="green",font=("sans serif", 12, "bold"),fg_color="white", command=self.clear,
                                                    corner_radius=20, width=110)
        self.buttonEffacer.place(x=480, y=450)


      # =========================Recherche=======================

        self.var_recherche = StringVar()
        label_recherche = ct.CTkLabel(self.mac, text="Matricule", font=("sans serif", 15, "bold"))
        label_recherche.place(x=720, y=20)

        entry_recherche = ct.CTkEntry(self.mac, font=("sans serif", 15, "bold"), textvariable=self.var_recherche, width=200)
        entry_recherche.place(x=830, y=20)
        

        buttonSearch = ct.CTkButton(self.mac, text="Rechercher", text_color="white",font=("sans serif", 12, "bold"),fg_color="green", command=self.search,
                                                    corner_radius=20, width=110)
        buttonSearch.place(x=1050, y=20)



        self.C_Frame = Frame(self.mac, bd=2, relief=RIDGE)
        self.C_Frame.place(x=620, y=60, width=570, height=440)

        Scroll_y = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scroll_x = Scrollbar(self.C_Frame, orient=HORIZONTAL)


        self.EtudiantsTable = ttk.Treeview(self.C_Frame, column=("Matricule", "Nom", "Prénom", "Email","Sexe", "Niveau", "Date de Naissance", "Contacte","Cour","Date Adminssion","Ville","Pin Code", "Adresse"),
                                                      xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.EtudiantsTable.xview)
        Scroll_y.config(command=self.EtudiantsTable.yview)

        self.EtudiantsTable.heading("Matricule", text="Matricule")
        self.EtudiantsTable.heading("Nom", text="Nom")
        self.EtudiantsTable.heading("Prénom", text="Prénom")
        self.EtudiantsTable.heading("Email", text="Email")
        self.EtudiantsTable.heading("Sexe", text="Sexe")
        self.EtudiantsTable.heading("Niveau", text="Niveau")
        self.EtudiantsTable.heading("Date de Naissance", text="Né(e) le")
        self.EtudiantsTable.heading("Contacte", text="Contat")
        self.EtudiantsTable.heading("Cour", text="Cour")
        self.EtudiantsTable.heading("Date Adminssion", text="Date Admission")
        self.EtudiantsTable.heading("Ville", text="Ville")
        self.EtudiantsTable.heading("Pin Code", text="Pin Code")
        self.EtudiantsTable.heading("Adresse", text="Adresse")
        
        self.EtudiantsTable["show"]="headings"
        
        self.EtudiantsTable.column("Matricule", width=150)
        self.EtudiantsTable.column("Nom", width=150)
        self.EtudiantsTable.column("Prénom", width=150)
        self.EtudiantsTable.column("Email", width=150)
        self.EtudiantsTable.column("Sexe", width=150)
        self.EtudiantsTable.column("Niveau", width=150)
        self.EtudiantsTable.column("Date de Naissance", width=150)
        self.EtudiantsTable.column("Contacte", width=150)
        self.EtudiantsTable.column("Cour", width=150)
        self.EtudiantsTable.column("Date Adminssion", width=150)
        self.EtudiantsTable.column("Ville", width=150)
        self.EtudiantsTable.column("Pin Code", width=150)
        self.EtudiantsTable.column("Adresse", width=150)
       
        self.EtudiantsTable.pack(fill=BOTH, expand=1)
        self.EtudiantsTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def get_data(self, ev):
      self.txt_NumMat.configure(state="readonly")
      r = self.EtudiantsTable.focus()
      content = self.EtudiantsTable.item(r)
      row = content["values"]

      self.var_matricule.set(row[0])
      self.var_Nom.set(row[1])
      self.var_Prenom.set(row[2])
      self.var_Email.set(row[3])
      self.var_sexe.set(row[4])
      self.var_Niveau.set(row[5])
      self.var_DateNaiss.set(row[6])
      self.var_Contact.set(row[7])
      self.var_CoursSelect.set(row[8])
      self.var_Date_Admission.set(row[9])
      self.var_Ville.set(row[10])
      self.var_Pin.set(row[11])
      self.txt_Adresse.delete('1.0', END)
      self.txt_Adresse.insert(END, row[12])


    def add(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            if self.var_matricule.get()=="" or self.var_Nom.get()=="" or self.var_Prenom.get()=="":
              messagebox.showerror("Erreur", "Entrez le nom du Cour.", parent=self.mac)
            else:
              query = "select * from Etudiants where NumMat=?"
              cur.execute(query, (self.var_matricule.get(),))
              row=cur.fetchone()
              if row !=None:
                messagebox.showerror("Erreur", "Le cour saisi est existe déja", parent=self.mac)
              else:

                query = "insert into Etudiants (NumMat, Nom, Prenom, Email, Sexe, DateNaiss, Contact, Cours_Select, Date_Admission, Niveau, Ville, Pin, Adresse) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                values = (self.var_matricule.get(),
                          self.var_Nom.get(),
                          self.var_Prenom.get(),
                          self.var_Email.get(),
                          self.var_sexe .get(),
                          self.var_Niveau.get(),
                          self.var_DateNaiss.get(),
                          self.var_Contact.get(),
                          self.var_CoursSelect.get(),
                          self.var_Date_Admission.get(),
                          self.var_Ville.get(),
                          self.var_Pin.get(),
                          self.txt_Adresse.get("1.0", END))

                cur.execute(query, values)
                conn.commit()
                messagebox.showinfo("succes", "Etudiant Ajouter avec Succès", parent=self.mac)
                self.show()
                self.clear()
          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)


    def show(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            query = "select * from Etudiants"
            cur.execute(query)
            rows=cur.fetchall()
            self.EtudiantsTable.delete(*self.EtudiantsTable.get_children())

            for row in rows:
              self.EtudiantsTable.insert('', END,values=row)

          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)


    def Update(self):
          conn = sqlite3.connect(database="school_managment.db")
          cur = conn.cursor()

          try:
            if self.var_matricule.get()=="":
              messagebox.showerror("Erreur", "Matricule Obligatoire", parent=self.mac)
            else:
              query = "select * from Etudiants where NumMat=?"
              cur.execute(query, (self.var_matricule.get(),))
              row=cur.fetchone()
              if row == None:
                messagebox.showerror("Erreur", "Sélecctionnez un cour dans la liste", parent=self.mac)
              else:

                query = "update Etudiants set Nom=?, Prenom=?, Email=?, Sexe=?, DateNaiss=?, Contact=?, Cours_Select=?, Date_Admission=?, Niveau=?, Ville=?, Pin=?, Adresse=? where NumMat=?"
                values = (self.var_Nom.get(),
                          self.var_Prenom.get(),
                          self.var_Email.get(),
                          self.var_sexe.get(),
                          self.var_Niveau.get(),
                          self.var_DateNaiss.get(),
                          self.var_Contact.get(),
                          self.var_CoursSelect.get(),
                          self.var_Date_Admission.get(),
                          self.var_Ville.get(),
                          self.var_Pin.get(),
                          self.txt_Adresse.get("1.0", "end-1c"),
                          self.var_matricule.get())
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
            if self.var_matricule.get()=="" or self.var_Nom.get()=="":
              messagebox.showerror("Erreur", "Entrez le Matricule de l'Etudiant.", parent=self.mac)
            else:
              query = "select * from Etudiants where NumMat=?"
              cur.execute(query, (self.var_matricule.get(),))
              row=cur.fetchone()
              if row ==None:
                messagebox.showerror("Erreur", "svp sélectionnez un Etudiant dans la liste", parent=self.mac)
              else:
                op = messagebox.askyesno("Attention", "voulez Vraiment Supprimer cet Etudiants ?", parent=self.mac)
                if op == True:
                  query = "delete from Etudiants where NumMat=?"
                  value = (self.var_matricule.get(),)
                  cur.execute(query, value)
                  conn.commit()
                  messagebox.showinfo("Succès", "Etudiant supprimr avec succès")
                  self.clear()
                  self.show()
        except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)


    def clear(self):
      self.show()
      self.var_matricule.set("")
      self.var_Nom.set("")
      self.var_Prenom.set("")
      self.var_Email.set("")
      self.var_sexe.set("Masculin")
      self.var_Niveau.set("Licence/BTS/Master")
      self.var_DateNaiss.set("")
      self.var_Contact.set("")
      self.var_CoursSelect.set("Cours")
      self.var_Date_Admission.set("")
      self.var_Ville.set("")
      self.txt_Adresse.delete("1.0", "end")
      self.txt_Adresse.insert("1.0", "")

      x = rd.randint(1000, 9999)
      self.var_Pin.set(str(x))


   

    def search(self):
      conn = sqlite3.connect(database="school_managment.db")
      cur = conn.cursor()

      try:
          query = "SELECT * FROM Etudiants WHERE NumMat LIKE ?"
          search_term = '%' + self.var_recherche.get() + '%'
          cur.execute(query, (search_term,))
          rows = cur.fetchall()
          self.EtudiantsTable.delete(*self.EtudiantsTable.get_children())

          for row in rows:
              self.EtudiantsTable.insert('', END, values=row)

      except Exception as ex:
          messagebox.showerror("Erreur", f"Erreur due à {str(ex)}", parent=self.mac)







if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Etudiants(Mac)
    Mac.mainloop()