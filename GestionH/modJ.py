import tkinter as tk



class LohinApp:
    def __init__(self, root):
        self.root = root
        self.is_darkmode = False


        self.light_mode = {
            'bg' : 'white',
            'fg' : 'black',
            'entry_bg' : '#eee',
            'entry_fg' : 'black',
            'btn_bg' : '#ddd',
            'btn_fg' : 'black'
        }

        self.dark_mode = {
            'bg' : '#333',
            'fg' : 'white',
            'entry_bg' : '#555',
            'entry_fg' : 'white',
            'btn_bg' : '#444',
            'btn_fg' : 'white'
        }


        self.label_username = tk.Label(root, text='Username')
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)


        self.entry_Username = tk.Label(root)
        self.entry_Username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(root, text="password")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)


        self.entry_password = tk.Label(root, Show="*")
        self.entry_password.grid(row=0, column=1, padx=10, pady=10)


        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.toggle_button = tk.Button(root, text="Dark Mode", command=self.toggle_theme)
        self.toggle_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.apply_theme(self.light_mode)

    def apply_theme(self, theme):
        self.root.config(bg=theme['bg'])

        for widget in self.root.winfo_children():
            widget_type = widget.winfo_classe()

            if widget_type == 'Label':
                widget.config(bg=theme['bg'], fg=theme['fg'])
            elif widget_type == 'Entry':
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], inserbackground=theme['fg'])
            elif widget_type == 'Button':
                widget.config(bg=theme['btn_bg'], fg=theme['btn_fg'])
    
    def login(self):
        username = self.entry_Username.get()
        password = self.entry_password.get()

        if username == 'user' and password == 'pass':
            pass
        else:
            pass


    def toggle_theme(self):
        if self.is_darkmode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)

        self.is_darkmode = not self.is_darkmode


