import customtkinter as ct
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class ToDoList:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("To Do List wise Mister Py🐍")
        self.mac.geometry("500x500")
        self.mac.resizable(0,0)

        #Variables 
        self.Tasks = StringVar()
        self.Date = StringVar()
        self.Description = StringVar()

        #Frame Add Tasks

        AddFrame = ct.CTkFrame(self.mac, width=450, height=80, corner_radius=20)
        AddFrame.grid(row=0, column=0, pady=5, padx=10)

        EntryTask = ct.CTkEntry(AddFrame, placeholder_text="Ajouter Une Tache", font=("sans serif", 13),  textvariable=self.Tasks, width=150, corner_radius=20)
        EntryTask.grid(row=0, column=0, pady=5, padx=5)

        EntryDate = ct.CTkEntry(AddFrame, placeholder_text="Date", font=("sans serif", 13), textvariable=self.Date, width=150, corner_radius=20)
        EntryDate.grid(row=0, column=1, pady=5, padx=5)

        # EntryDescription = ct.CTkEntry(AddFrame, placeholder_text="Heure", font=("sans serif", 13),textvariable=self.Description, width=150, corner_radius=20)
        # EntryDescription.grid(row=0, column=2, pady=5, padx=5)

        self.textbox = ct.CTkTextbox(self.mac, width=150, height=100)
        self.textbox.grid(row=0, column=2, pady=5, padx=5)
        self.textbox.insert("0.0", "")

    

        ButtonAddTask = ct.CTkButton(AddFrame, text="Add", font=("sans serif", 14), width=100, corner_radius=20, command=self.add)
        ButtonAddTask.grid(row=1, column=1, pady=5, padx=5)

        ButtonDeleteTask = ct.CTkButton(AddFrame, text="Delete", font=("sans serif", 14), width=100, corner_radius=20, command=self.delete)
        ButtonDeleteTask.grid(row=2, column=1, pady=5, padx=5)

        self.appearance_mode_optionemenu = ct.CTkOptionMenu(AddFrame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=1)




        #Board Tasks


        self.C_Frame = Frame(self.mac, bd=2, relief=RIDGE)
        self.C_Frame.place(x=15, y=180, width=470, height=240)

        Scroll_y = Scrollbar(self.C_Frame, orient=VERTICAL)
        Scroll_x = Scrollbar(self.C_Frame, orient=HORIZONTAL)


        self.CourseTable = ttk.Treeview(self.C_Frame, column=("cid", "nom", "Date", "Description", "Etat"),
                                                      xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.CourseTable.xview)
        Scroll_y.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="Nº")
        self.CourseTable.heading("nom", text="Nom")
        self.CourseTable.heading("Date", text="Date")
        self.CourseTable.heading("Description", text="Description")
        self.CourseTable.heading("Etat", text="Etat")
        
        self.CourseTable["show"]="headings"
        
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("nom", width=100)
        self.CourseTable.column("Date", width=100)
        self.CourseTable.column("Description", width=150)
        self.CourseTable.column("Etat", width=100)
       
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()






    def change_appearance_mode_event(self, new_appearance_mode: str):
        ct.set_appearance_mode(new_appearance_mode)

    def get_data(self, event):
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        
        # self.txt_description.delete('1.0', END)
        # self.txt_description.insert(END, row[4])
       
        row = content["values"]
        self.Tasks.set(row[0])
        self.Date.set(row[1])
        self.textbox.set(row[2])





    def add(self):
        conn = sqlite3.connect(database="To_DoList.db")
        cur = conn.cursor()

        try:
            if self.Tasks.get() == "" or self.Date.get() == "" or self.textbox.get() == "":
                messagebox.showerror("Erreur", "Entrez La Tache svp", parent=self.mac)
            else:
                query = "select * from Tasks where nom=?"
                cur.execute(query, (self.Tasks.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Erreur", "La tache saisi existe déja hein", parent=self.mac)
                else:

                    query = "insert into Tasks (nom, Date, Description, Etat) values(?, ?, ?)"
                    values = (self.Tasks.get(),
                              self.Date.get(),
                              self.textbox.get()

                            )
                    
                    cur.execute(query, values)
                    conn.commit()
                    messagebox.showinfo("Reussi", "Succès", parent=self.mac)
                    self.show()
        except Exception as es:
            messagebox.showerror("Erreur", f"Erreur du a {str(es)}", parent=self.mac)
    
    def delete(self):
        conn = sqlite3.connect(database="To_DoList.db")
        cur = conn.cursor()

        try:
            if self.Tasks.get() == "" or self.Date.get() == "" or self.textbox.get() == "":
                messagebox.showerror("Erreur", "Entrez La Tache svp", parent=self.mac)
            else:
                query = "select * from Tasks where nom=?"
                cur.execute(query, (self.Tasks.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Erreur", "Séléctionne une tache", parent=self.mac)
                else:
                    op = messagebox.askyesno("Attention", "Voulez vous Supprimer ?", parent=self.mac)
                    if op == True:
                        query = "delete from Tasks where nom=?"
                        value = (self.Tasks.get(),)
                        cur.execute(query, value)
                        conn.commit()
                        messagebox.showinfo("Succès", "Tache Supprimer avec succès", parent=self.mac)
                        self.show()
        except Exception as es:
            messagebox.showerror("Erreur", f"Erreur du a {str(es)}", parent=self.mac)





    # def show(self):
    #     conn = sqlite3.connect(database="To_DoList.db")
    #     cur = conn.cursor()

    #     try:
    #         query = "select * from Tasks"
    #         cur.execute(query)
    #         rows = cur.fetchall()

    #         for widget in self.BoardTasks.winfo_children():
    #             widget.destroy()

    #         for row in rows:
    #             task_label = ct.CTkLabel(self.BoardTasks, text=row, padx=10, pady=5)
    #             task_label.pack(side=TOP, anchor=W)

    #     except Exception as es:
    #         messagebox.showerror("Erreur", f"Erreur du a {str(es)}", parent=self.mac)

    def show(self):
          conn = sqlite3.connect(database="To_DoList.db")
          cur = conn.cursor()

          try:
            query = "select * from Tasks"
    #       cur.execute(query)
    #       rows = cur.fetchall()
            cur.execute(query)
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
              self.CourseTable.insert('', END,values=row)

          except Exception as ex:
              messagebox.showerror("Erreur", f"Erreur dû a {str(ex)}", parent=self.mac)



if __name__ == "__main__":
    Mac = ct.CTk()
    obj = ToDoList(Mac)
    Mac.mainloop()
