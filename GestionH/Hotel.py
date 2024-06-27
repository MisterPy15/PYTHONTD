from tkinter import *
import customtkinter as ct
from PIL import Image,ImageTk
from time import strftime
from Clients import Client_fenetre
from Chambre import chambre_fenetre
from Detail import Detail_fenetre
from Rapport import Rapport_fenetre



ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

class HotelManagementSystem:

    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Gestion D'Hotel façon Mister Py 🐍")
        self.mac.geometry("1600x750+0+0")
        # self.mac.resizable(1,1)





        def  heure():
            heur = strftime("%H : %M : %S ")
            labelHeure.config(text=heur)
            labelHeure.after(1000, heure)



        labelHeure = Label(self.mac, text="HH : MM : SS", font=("sans serif", 25, "bold"),
                                     bd=4,fg="green", bg="black", relief=RIDGE)
        labelHeure.place(x=0, y=120, width=200, height=40)
        heure()

        def scroll_text():
            global text
            text = labelTitle.cget("text")
            text = text[1:] + text[0]  
            labelTitle.config(text=text)
            labelTitle.after(200, scroll_text)

        text = "GESTION D'HOTEL FAÇON MISTER PY 🐍"
        labelTitle = Label(self.mac, text=text, font=('sans serif', 22, 'bold'),
                                        bg="black", fg="white", bd=4, relief=RIDGE)
        labelTitle.place(x=200, y=120, width=1165, height=40)

        scroll_text()



        img1 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/log1.jpeg")
        img1 = img1.resize((1185,120))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        labelimage1 = Label(self.mac, image=self.photoimg1, bd=4, relief=RIDGE)
        labelimage1.place(x=180, y=0, width=1185, height=120)


        img2 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/logo2.webp")
        img2 = img2.resize((180,120))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        labelimage = Label(self.mac, image=self.photoimg2, bd=4, relief=RIDGE)
        labelimage.place(x=0, y=0, width=180, height=120)


    
        # ==================================Main Frame=============================== 
        main_Frame = Frame(self.mac, bd=4, relief=RIDGE)
        main_Frame.place(x=0, y=160, width=1363, height=610)



        # =========================Menu ===============================
        labelMenu = Label(main_Frame, text="MENU", font=('sans serif', 17, 'bold'),
                                     bg="black", fg="white", bd=4, relief=RIDGE)
        labelMenu.place(x=0, y=0, width=230, height=40)



        # ====================btn Frame ===================================

        btn_frame = Frame(main_Frame,bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=40, width=228, height=200)

       

        client_btn = ct.CTkButton(btn_frame, text="CLIENTS", text_color="white",  fg_color="black" ,width=220,
                                             command=self.client_detail, font=('sans serif', 14, 'bold'),
                                            cursor="hand1", corner_radius=10)
        client_btn.grid(row=0, column=0, pady=5)
        
        
        


        romm_btn = ct.CTkButton(btn_frame, text="CHAMBRE", text_color="white", fg_color="black" , width=220, 
                                                command=self.room_detail, font=('sans serif', 14, 'bold'),
                                                cursor="hand1", corner_radius=10)
        romm_btn.grid(row=1, column=0, pady=5)


        details_btn = ct.CTkButton(btn_frame, text="DETAILS", text_color="white", fg_color="black" , width=220, 
                                                command=self.detail_D, font=('sans serif', 14, 'bold'), 
                                                cursor="hand1", corner_radius=10)
        details_btn.grid(row=2, column=0, pady=5)


        report_btn = ct.CTkButton(btn_frame, text="FACTURE", text_color="white", fg_color="black" , width=220,
                                                command=self.report_detail, font=('sans serif', 14, 'bold'),
                                                cursor="hand1", corner_radius=10)
        report_btn.grid(row=3, column=0, pady=5)


        logout_btn = ct.CTkButton(btn_frame, text="QUITTER", text_color="white", fg_color="black" , width=220,
                                                command=self.logout_Functun,font=('sans serif', 14, 'bold'), 
                                                cursor="hand1", corner_radius=10)
        logout_btn.grid(row=4, column=0, pady=5)



        img3 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/im4.jpg")
        img3 = img3.resize((1123,700))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        labelimage = Label(main_Frame, image=self.photoimg3, bd=4, relief=RIDGE)
        labelimage.place(x=230, y=0, width=1123, height=600)
        




        img4 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/im8.jpg")
        img4 = img4.resize((230,290))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        labelimage = Label(main_Frame, image=self.photoimg4, bd=4, relief=RIDGE)
        labelimage.place(x=0, y=240, width=230, height=290)



        # img5 = Image.open(r"/Users/misterpy/desktop/TD_PYTHON/GestionH/Image/imN2.jpeg")
        # img5 = img5.resize((230,165))
        # self.photoimg5 = ImageTk.PhotoImage(img5)

        # labelimage = Label(main_Frame, image=self.photoimg5, bd=4, relief=RIDGE)
        # labelimage.place(x=0, y=370, width=230, height=165)





    def client_detail(self):
        self.nouvelle_fenetre = Toplevel(self.mac)
        self.app = Client_fenetre(self.nouvelle_fenetre)

    def room_detail(self):
        self.Chambre_fenetre = Toplevel(self.mac)
        self.app = chambre_fenetre(self.Chambre_fenetre)

    def detail_D(self):
        self.Detail_fenetre = Toplevel(self.mac)
        self.app = Detail_fenetre(self.Detail_fenetre)
   
    def report_detail(self):
        self.Rapport_fenetre =  Toplevel(self.mac)
        self.app = Rapport_fenetre(self.Rapport_fenetre)
    
    def logout_Functun(self):
        self.mac.destroy()
        

       












if __name__ == "__main__":
    Mac = ct.CTk()
    obj = HotelManagementSystem(Mac)
    Mac.mainloop()