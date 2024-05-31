import customtkinter
import random

from func import guess_the_number

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk() 
app.geometry("400x240")

computer_n = random.randrange(1,10)

play=True
lives=3

def button_function():
    global computer_n, lives, lower, larger, play
    if play:
        if int(entry.get()) == computer_n:
            label.configure(text='YOU WIN!!!')
            
            play = False
            
        else:
            
            if int(entry.get()) < computer_n:
                lives -= 1
                
                label.configure(text='Number is larger!')
            else:
                lives -= 1
                
                label.configure(text='Number is larger!')
            
            if lives == 0:
                play = False   
    else:
        label.configure(text='YOU LOSE!!!')
        
    print("button pressed")

entry = customtkinter.CTkEntry(app, placeholder_text="Enter num 1-10")
entry.pack(fill="x", pady=20)

button = customtkinter.CTkButton(master=app, text="Pass", command=button_function)
button.pack(pady=5)

label = customtkinter.CTkLabel(app, text="", fg_color="transparent", width=100, height=100)
label.pack(pady=10)

app.mainloop()