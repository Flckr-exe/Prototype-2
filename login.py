import customtkinter
import os 

customtkinter.set_appearance_mode("black")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.geometry("350x350")

def login():
    entered_username = entry1.get()
    entered_password = entry2.get()

    if entered_username == "Admin" and entered_password == "admin":
        print("Login successful")
        root.destroy()  
        open_app()      
    else:
        print("Invalid username or password")
        

def open_app():
    os.system("python app.py")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=10, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

root.mainloop()

