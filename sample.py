from tkinter import *
from PIL import ImageTk, Image
from read import *
from tkinter import messagebox
import sqlite3
import customtkinter

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")

class SampleApp:

    def __init__(self, window, title):
        conn = sqlite3.connect("Attendence.db")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                id INTEGER PRIMARY KEY,
                StudentName text
            )""")
        username = StringVar()
        self.window = window
        self.title = title
        window.title(self.title)
        window.geometry("400x300")
        window.iconbitmap("icon.ico")
        window.config(bg="black")
        self.frame = customtkinter.CTkFrame(master=window)
        self.frame.pack(pady=20, padx=10, fill='both', expand=True)

        self.lbl = customtkinter.CTkLabel(master=self.frame, text="Train Data")
        self.namelbl = customtkinter.CTkLabel(master=self.frame, text="Enter Student Name")
        self.UserNameEntry = customtkinter.CTkEntry(master=self.frame)
        self.TakePhotoBtn  = customtkinter.CTkButton(master=self.frame, text="Take Photo Sample", command=lambda:insertStudentData(self))
        self.lbl.grid(row=0, columnspan=2, pady=12, padx=10)
        self.namelbl.grid(row=1, column=0, pady=12, padx=10)
        self.UserNameEntry.grid(row=1, column=1, pady=12, padx=10)
        self.TakePhotoBtn.grid(row=2, columnspan=2, pady=12, padx=10)

        def insertStudentData(self):
            c = conn.cursor()
            c.execute("INSERT INTO Student (StudentName) VALUES (:StudentName)",
            {
                'StudentName': self.UserNameEntry.get()
            }
            )
            conn.commit()
            # Get the ID of the last inserted row
            last_id = c.lastrowid
            print("The ID of the last inserted row is:", last_id)
            sampleData(self, last_id)

        def sampleData(self, id):
            print(self.UserNameEntry.get())
            if self.UserNameEntry.get() == "":
                messagebox.showerror("Missing","Enter the Name for the user")
            else:
                getData(self.UserNameEntry.get(), id)
                messagebox.showinfo("Success","Picture Sample Collected!")
                self.window.destroy()



# root = Tk()
# at = TrainApp(root, "Year 11")
# root.mainloop()