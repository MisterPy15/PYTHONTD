# import qrcode

# def generate_qr_code(Nom,Prenom,Numero, filename):
#     qr = qrcode.QRCode(
#         version=5,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(Nom)
#     qr.add_data(Prenom)
#     qr.add_data(Numero)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="white", back_color="black")
#     img.save(filename)

# Nom = "  Mister "
# Prenom = " Py \n"
# Numero = "0778748602"
# filename = "Info.png"
# generate_qr_code(Nom,Prenom,Numero, filename)
# print(f"QR code généré et enregistré sous le nom de fichier : {filename}")









import customtkinter as ctk
import qrcode

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("300x200")

        self.label = ctk.CTkLabel(self.root, text="Texte à encoder:")
        self.label.pack()

        self.entry = ctk.CTkEntry(self.root)
        self.entry.pack()

        self.button = ctk.CTkButton(self.root, text="Générer QR Code", command=self.generate_qr_code)
        self.button.pack()

    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")
            ctk.messagebox.showinfo("QR Code généré", "QR Code généré et enregistré sous le nom de fichier : qrcode.png")
        else:
            ctk.messagebox.showwarning("Texte manquant", "Veuillez entrer un texte à encoder.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()