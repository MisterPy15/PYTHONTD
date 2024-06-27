from tkinter import *
from customtkinter import *


class Admin:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Admin")
        self.mac.geometry("850x850") #Taille de La fenêtre
        # self.mac.resizable(0,0)
        self.mac.configure(bg="#23272A")

        self.label = CTkLabel(self.mac, text="Admin", font=("Roboto Medium", 16))
        self.label.place(relx=0.5, rely=0.1, anchor=CENTER)





if __name__ =="__main__":
    Mac= CTk()
    obj = Admin(Mac)
    Mac.mainloop()