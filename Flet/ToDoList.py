import flet as ft


def main(page: ft.Page):

    # text = ft.Text(value="Bonjour Je Suis Mister Py", color="white")
    # page.controls.append(text)
    # page.update()
<<<<<<< HEAD
 
=======

>>>>>>> c739d220f8696e11e0686d52345056f08433c336
    def Ajout_Tache(e):
        page.add(ft.Checkbox(label=nouvelle_tache.value))
        nouvelle_tache.value = ""
        nouvelle_tache.focus()
        nouvelle_tache.update()

        # if nouvelle_tache.get() == "":
                
            

    nouvelle_tache = ft.TextField(hint_text="Ajoute Une tâche", width=350)
    page.add(ft.Row([nouvelle_tache, ft.ElevatedButton("Ajouter", on_click=Ajout_Tache)]))




# Pour l'afficher en version Desktop
<<<<<<< HEAD
# ft.app(target=main)

# Pour l'afficher en version Web
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
=======
ft.app(target=main)

# Pour l'afficher en version Web
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
>>>>>>> c739d220f8696e11e0686d52345056f08433c336
