import customtkinter as ct
from pytube import Playlist, YouTube
import re
from tkinter import filedialog, messagebox

class Telechargement:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("Youtube Download Playlist wise Mister Py🐍")
        self.mac.geometry("700x300")
        self.mac.resizable(0, 0)

        labeTitle = ct.CTkLabel(self.mac, text="🐍", font=("Sans serif", 30))
        labeTitle.place(x=330, y=0)

        labelLink = ct.CTkLabel(self.mac, text="lien de la playlist", font=("sans serif", 15, "bold"))
        labelLink.place(x=20, y=100)

        self.entryLink = ct.CTkEntry(self.mac, font=("sans serif", 13, "bold"), placeholder_text="coller le lien", width=300, corner_radius=20)
        self.entryLink.place(x=160, y=100)

        buttonDown = ct.CTkButton(self.mac, text="Télécharger", font=("san francisco", 14, "bold"), corner_radius=20, width=150, command=self.telechargement)
        buttonDown.place(x=470, y=100)




    def telechargement(self):
        url_playlist = self.entryLink.get()

        try:
            if url_playlist == "":
                messagebox.showerror("Erreur", "Veuillez coller le lien svp", parent=self.mac)
                return

            playlist = Playlist(url_playlist)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            videos = playlist.video_urls

            destination_folder = filedialog.askdirectory()

            if destination_folder:
                for video_url in videos:
                    video = YouTube(video_url)
                    video_stream = video.streams.filter(file_extension='mp4', res='720p')
                    video_stream = video_stream.first()
                    if video_stream:
                        video_stream.download(output_path=destination_folder)
                    else:
                        messagebox.showerror("Erreur", "Aucune Vidéo MP4 HD Trouvée.", parent=self.mac)
        except Exception as es:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(es)}", parent=self.mac)




if __name__ == "__main__":
    Mac = ct.CTk()
    obj = Telechargement(Mac)
    Mac.mainloop()
