from tkinter import *
import customtkinter as ct

class MyApp:
    def __init__(self, app):
        self.app = app
        self.app.geometry("300x600")
        self.todolist = []
        self.initvalue = StringVar()


        self.txt = ct.CTkEntry(self.app, placeholder_text="tache", textvariable=self.initvalue, font=("times", 35))
        self.txt.pack(pady=20)

        self.button = ct.CTkButton(self.app, text="Add", command=self.addnew)
        self.button.pack(pady=10)

        self.frame = ct.CTkFrame(self.app, fg_color="blue")
        self.frame.pack(fill=BOTH, expand=True)


    def addnew(self):
        value = self.initvalue.get()
        self.todolist.append({"name":value})
        print(self.todolist)

        self.display_Todolist()

    def display_Todolist(self):
        for w in self.frame.winfo_children():
            w.destroy()
        
        for i,item in enumerate(self.todolist):
            frame = ct.CTkFrame(self.frame)
            frame.pack(fill="both", pady=15, padx=20)

            label = ct.CTkLabel(frame, text=item['name'], font=("times", 20))
            label.pack(sid="top", padx=5, pady=15)

            edit = ct.CTkButton(frame, text="Edit", fg_color="blue", command=lambda idx=i:self.edit_item(idx))
            edit.pack(side="left", padx=5, pady=15)

            delete = ct.CTkButton(frame, text="Delete", fg_color="red", command=lambda idx=i:self.delete_item(idx))
            delete.pack(side="left", padx=5, pady=15)
    

    def edit_item(self, index):
        if index < len(self.todolist):
            item = self.todolist[index]
            item_name = item['name']
            self.initvalue = item_name
            self.bt.configure(text="Update", tetx_color="black", fg_color="yellow", command=lambda idx=index:self.update_item(idx))

        else:
            print("invalid index you ...")


    def update_item(self, index):
        if index < len(self.todolist):
            update_value = self.txt.get()
            self.todolist[index]['name']= update_value
            self.display_Todolist
            self.bt.configure(text="Update", tetx_color="black",
                                             fg_color="blue", command=self.addnew)
        else:
            print("invalid index")




    def delete_item(self, index):
        pass
    



if __name__ == "__main__":
    app = ct.CTk()
    obj = MyApp(app)
    app.mainloop()