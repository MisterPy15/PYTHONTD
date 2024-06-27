import customtkinter as ct
import tkinter as tk 
# from PIL import ImageTk, Image
# import pymysql



class FibreOptic:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Admin Fiber Box")
        self.mac.geometry("850x425")
        self.mac.resizable(0,0)


        # frame_Fonctionnalite = ct.CTkFrame(master=mac, height=425, width=300, corner_radius=30, bg_color="white")
        # frame_Fonctionnalite.grid(row=0, column=0)

        tabView = ct.CTkTabview(mac, height=420, width=850, corner_radius=30, bg_color="blue")
        tabView.grid(row=0, column=0)
        tabView.add("Appareils Connecter")
        tabView.add("Paramètre de la Box")

        label_Total_Appareils_connecter = ct.CTkLabel(tabView.tab("Appareils Connecter"),text="Total Apareil connecter : 0", font=("sans serif", 18, "bold"))
        label_Total_Appareils_connecter.grid(row=0, column=0)

        # frame_liste_Appareil_connecter = ct.CTkLabelFrame(tabView.tab("Appareils Connecter"), text="Liste des Appareil")
        frame_liste_Appareil_connecter = ct.CTkScrollableFrame(tabView.tab("Appareils Connecter"), bg_color="gray", corner_radius=40)
        frame_liste_Appareil_connecter.grid(row=2, column=2)


        # label_Liste_Appareils_connecter = ct.CTkLabel(tabView.tab("Appareils Connecter"),text="Total Apareil connecter : 0", font=("sans serif", 15, "bold"))
        # label_Liste_Appareils_connecter.grid(row=2, column=1)
        
        









if __name__ == "__main__":
    Mac = ct.CTk()
    Obj = FibreOptic(Mac)
    Mac.mainloop()