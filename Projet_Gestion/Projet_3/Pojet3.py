import customtkinter as ct
import tkinter as tk

class Hotel:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion Hotel")
        self.master.geometry('1300x700')
        self.master.resizable(0,0)
        # self.master.grid_columnconfigure(0, weight=0)
        # self.master.grid_columnconfigure(1, weight=1)

        self.master.grid_columnconfigure(1, weight=0)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
       

        

        # Barre de Navigation
        # self.navigation_frame = ct.CTkFrame(self.master, corner_radius=10)
        # self.navigation_frame.grid(row=0, column=0)
        # self.navigation_frame.grid_rowconfigure(100, weight=1)

        self.navigation_frame = ct.CTkFrame(self.master, width=140, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        

        self.navigation_frame_label = ct.CTkLabel(self.navigation_frame, text="  MENU",
                                                  font=ct.CTkFont(size=35, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.client_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="Client", fg_color="transparent", font=("sans serif", 18),
                                        text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w", command=self.client_button_event)
        self.client_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Chambres", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Details", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Factures", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Quitter", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        # Mode nuit et mode jour
        self.appearance_mode_menu = ct.CTkOptionMenu(self.navigation_frame,
                                        values=["Dark", "Light", "System"],
                                        command=self.Mode_Nuit_Jour)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        #Zoom
        self.scaling_optionemenu = ct.CTkOptionMenu(self.navigation_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, sticky="s")






        # Create client  frame

        self.client_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.client_frame.grid_columnconfigure(0, weight=0)

        self.client_frame_labelX = ct.CTkLabel(self.client_frame, text="GESTION D'HÔTEL", font=("sans serif bold", 50))
        self.client_frame_labelX.grid(row=0, column=5)


        self.client_label_frame1 = ct.CTkScrollableFrame(self.client_frame, label_text="INFORMATION DU CLIENT")
        self.client_label_frame1.grid(row=2, column=1)

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Réf Client")
        self.client_entry_Ref.grid(row=0, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Nom Client")
        self.client_entry_Ref.grid(row=1, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Prénom Client")
        self.client_entry_Ref.grid(row=2, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_Option_Sexe= ct.CTkOptionMenu(self.client_label_frame1, values=["Sélectionne", "Homme", "Femme"])         
        self.client_Option_Sexe.grid(row=3, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Contacte")
        self.client_entry_Ref.grid(row=4, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Nationnalité")
        self.client_entry_Ref.grid(row=5, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Pièce d'identité")
        self.client_entry_Ref.grid(row=6, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Num Pièce Id")
        self.client_entry_Ref.grid(row=7, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")

        self.client_entry_Ref = ct.CTkEntry(self.client_label_frame1, placeholder_text="Adresse")
        self.client_entry_Ref.grid(row=8, column=0, columnspan=2, padx=(5, 0), pady=(2, 2), sticky="nsew")


        self.client_button1 = ct.CTkButton(self.client_frame, text="Save")
        self.client_button1.grid(row=10, column=0)

        self.client_button2 = ct.CTkButton(self.client_frame, text="Update")
        self.client_button2.grid(row=11, column=1)

        self.client_button3 = ct.CTkButton(self.client_frame, text="Delete")
        self.client_button3.grid(row=12, column=0)

        self.client_button4 = ct.CTkButton(self.client_frame, text="Reset")
        self.client_button4.grid(row=13, column=1)




        # Create Rooms frame
        self.second_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")






        # Create Details frame
        self.third_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")

        #Create bills frame
        self.third_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")

        #Create Button function quit
        # self.third_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("client")

    def select_frame_by_name(self, name):
        # Hide all frames
        self.client_frame.grid_forget()
        self.second_frame.grid_forget()
        self.third_frame.grid_forget()

        # Show selected frame
        if name == "client":
            self.client_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")

    def client_button_event(self):
        self.select_frame_by_name("client")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        # Add the appropriate function for the "Factures" button
        pass

    def frame_5_button_event(self):
        # Add the appropriate function for the "Quitter" button
        pass

    def client_frame_button_1_event(self):
        # Add the appropriate function for the first button in the client frame
        pass

    def client_frame_button_2_event(self):
        # Add the appropriate function for the second button in the client frame
        pass

    def client_frame_button_3_event(self):
        # Add the appropriate function for the third button in the client frame
        pass

    def client_frame_button_4_event(self):
        # Add the appropriate function for the fourth button in the client frame
        pass

    def Mode_Nuit_Jour(self, nouvel_apparence):
        ct.set_appearance_mode(nouvel_apparence)



    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ct.set_widget_scaling(new_scaling_float)




if __name__ == "__main__":
    Book = ct.CTk()
    obj = Hotel(Book)
    Book.mainloop()