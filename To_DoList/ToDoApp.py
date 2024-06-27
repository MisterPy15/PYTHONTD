import customtkinter as ct
import datetime as dt



class ToDolist:
    def __init__(self, mac):
        self.mac = mac
        self.mac.title("ToDolist wise Mister Py🐍")
        self.mac.geometry("650x600")
        # self.mac.resizable(0,0)
        self.todolist = []




        Title = ct.CTkLabel(self.mac, text="TO-DO List", font=("sans-ser",24, "bold"))
        Title.place(x=110, y=10)

        self.appearance_mode_optionemenu = ct.CTkOptionMenu(self.mac, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.place(x=280, y=10)

        self.EntryTasks = ct.CTkEntry(self.mac, placeholder_text="Add a new task", font=("sans-ser", 14, "bold"), width=450, height=40, corner_radius=7)
        self.EntryTasks.place(x=20, y=70)

        self.textbox = ct.CTkTextbox(self.mac, width=450, height=70)
        self.textbox.place(x=20, y=120)
        self.textbox.insert("0.0", "Description")


        ButtonAdd = ct.CTkButton(self.mac, text="Add Task", font=("sans-ser", 14, "bold"), width=80, height=40, fg_color="green", command=self.addnew)
        ButtonAdd.place(x=20, y=220)

        ButtonClear = ct.CTkButton(self.mac, text="Clear All", font=("sans-ser", 14, "bold"), width=80, height=40, fg_color="red")
        ButtonClear.place(x=390, y=220)

        frame_Title = ct.CTkFrame(self.mac, width=450, height=40, fg_color="blue")
        frame_Title.place(x=20, y=310) 

        textTask_frame = ct.CTkLabel(frame_Title, text="Task", font=("sans-ser", 18, "bold"), fg_color="blue")
        textTask_frame.place(x=10, y=5)


        textDate_frame = ct.CTkLabel(frame_Title, text="Due Date", font=("sans-ser", 18, "bold"), fg_color="blue")
        textDate_frame.place(x=190, y=5)


        textActions_frame = ct.CTkLabel(frame_Title, text="Actions", font=("sans-ser", 18, "bold"), fg_color="blue")
        textActions_frame.place(x=350, y=5)

        self.contentTaskFram = ct.CTkFrame(self.mac, width=620, corner_radius=10)
        self.contentTaskFram.place(x=20, y=350)

        # buttonContent = ct.CTkButton(contentTaskFrame, text="Done", width=60, height=40, fg_color="green")
        # buttonContent.place(x=305, y=10)


        # buttonContentDelete = ct.CTkButton(contentTaskFrame, text="Delete", width=60, height=40, fg_color="red")
        # buttonContentDelete.place(x=380, y=10)





    def addnew(self):
        value1 = self.EntryTasks.get()
        value2 = self.textbox.get("0.0", "end-1c")
        self.todolist.append({"name":value1, "description":value2})
        self.display_Todolist()

    def display_Todolist(self):
        for w in self.contentTaskFram.winfo_children():
            w.destroy()
        
        for i,item in enumerate(self.todolist):
            # frame = ct.CTkFrame(self.contentTaskFrame)
            # frame.pack(fill="both", pady=15, padx=20)

            self.contentTaskFrame = ct.CTkFrame(self.contentTaskFram, width=450, height=60, corner_radius=10, fg_color="#343434", border_width=2, border_color="gray")
            # self.contentTaskFrame.place(x=20, y=250)
            self.contentTaskFrame.pack(fill="both", pady=15, padx=20)

            label = ct.CTkLabel(self.contentTaskFrame, text=item['name'], font=("times", 20))
            label.pack(sid="top", padx=10, pady=15)

            label = ct.CTkLabel(self.contentTaskFrame, text=item['description'], font=("times", 20))
            label.pack(sid="top", padx=190, pady=15)

            buttonContent = ct.CTkButton(self.contentTaskFrame, text="Done", width=60, height=40, fg_color="green")
            buttonContent.place(x=305, y=10)

            buttonContentDelete = ct.CTkButton(self.contentTaskFrame, text="Delete", width=60, height=40, fg_color="red")
            buttonContentDelete.place(x=380, y=10)

    


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ct.set_appearance_mode(new_appearance_mode)


    # def frameAppearance(self):
    #     contentTaskFrame = ct.CTkFrame(self.mac, width=450, height=120, corner_radius=10, fg_color="transparent", border_width=2, border_color="gray")
    #     contentTaskFrame.place(x=20, y=370)

    #     buttonContent = ct.CTkButton(contentTaskFrame, text="Done", width=60, height=40, fg_color="green")
    #     buttonContent.place(x=380, y=10)


    #     buttonContentDelete = ct.CTkButton(contentTaskFrame, text="Delete", width=60, height=40, fg_color="red")
    #     buttonContentDelete.place(x=380, y=60)


if __name__ == "__main__":
    mac = ct.CTk()
    obj = ToDolist(mac)
    mac.mainloop()
