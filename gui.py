import customtkinter
import random

from func import guess_the_number, check_all

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk() 
app.geometry("400x240")

computer_n = random.randrange(1,10)

lower=False
larger=False
win=False
play=True
lives=3

def button_function():
    if play:
        guess_the_number(computer_n, entry.get(), lives, win, lower, larger, play)
        check_all(play, lower, larger, win, label)
    print("button pressed")

entry = customtkinter.CTkEntry(app, placeholder_text="Enter num 1-10")
entry.pack(fill="x", pady=20)

button = customtkinter.CTkButton(master=app, text="Pass", command=button_function)
button.pack(pady=5)

label = customtkinter.CTkLabel(app, text="Number lower", fg_color="transparent", width=100, height=100)
label.pack(pady=10)

app.mainloop()