import customtkinter as ct
import tkinter
import qrcode


class Hotel:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion Hotel")
        self.master.geometry('1000x700')
        self.master.resizable(0, 0)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
    
        #Mode nuit et mode jour
        self.appearance_mode_menu = ct.CTkOptionMenu(self.master,
                                        values=["Dark", "Light", "System"],
                                        command=self.Mode_Nuit_Jour)
        self.appearance_mode_menu.grid(row=4, column=0, padx=20, pady=20, sticky="s")



    




        #bar de Navigation

        self.navigation_frame = ct.CTkFrame(self.master, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0)
        self.navigation_frame.grid_rowconfigure(100, weight=0)

        self.navigation_frame_label = ct.CTkLabel(self.navigation_frame, text="  MENU",
                                                  compound="left", font=ct.CTkFont(size=35, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="Client", fg_color="transparent", font=("sans serif", 18),
                                        text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                        anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Chambres", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w")
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Details", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w")
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Factures", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w")
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = ct.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Quitter", fg_color="transparent", font=("sans serif", 18),
                                           text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w")
        self.frame_5_button.grid(row=5, column=0, sticky="ew")



        



        # create home frame
        self.home_frame = ct.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)


        self.home_frame_large_image_label = ct.CTkLabel(self.home_frame, text="Nombre d'Appareil connecté : 0")
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)



        self.home_frame_label_1 = ct.CTkLabel(self.home_frame, text="Appareil 1", font=("bold italic", 18))
        self.home_frame_label_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_1 = ct.CTkButton(self.home_frame, text="Détails", font=("bold italic", 13))
        self.home_frame_button_1.grid(row=1, column=1, padx=20, pady=10)



        self.home_frame_label_2 = ct.CTkLabel(self.home_frame, text="Appareil 2", font=("bold italic", 18))
        self.home_frame_label_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_2 = ct.CTkButton(self.home_frame, text="Détails", font=("bold italic", 13))
        self.home_frame_button_2.grid(row=2, column=1, padx=20, pady=10)



        self.home_frame_label_3 = ct.CTkLabel(self.home_frame, text="Appareil 3", font=("bold italic", 18))
        self.home_frame_label_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_3 = ct.CTkButton(self.home_frame, text="Détails", font=("bold italic", 13))
        self.home_frame_button_3.grid(row=3, column=1, padx=20, pady=10)


        self.home_frame_label_4 = ct.CTkLabel(self.home_frame, text="Appareil 4", font=("bold italic", 18))
        self.home_frame_label_4.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_button_4 = ct.CTkButton(self.home_frame, text="Détails", font=("bold italic", 13))
        self.home_frame_button_4.grid(row=4, column=1, padx=20, pady=10)



              # create second frame
        self.second_frame = ct.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = ct.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


    



    def Mode_Nuit_Jour(self, nouvel_apparence):
        ct.set_appearance_mode(nouvel_apparence)

    





if __name__ == "__main__":
    Book = ct.CTk()
    obj = Hotel(Book)
    Book.mainloop()