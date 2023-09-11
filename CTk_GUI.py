import customtkinter
from bard_AI import bard_GetAnswer


customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global entry
        self.grid_columnconfigure(0, weight=1)
        self.geometry("1000x600")
        self.title("Veg biriyani ahh")
        entry = customtkinter.CTkEntry(self, placeholder_text="Enter your prompt")
        entry.grid(row=0, column= 0, padx=20,pady=20,sticky = "ew", columnspan=2)

        searchButton = customtkinter.CTkButton(self, text= "Ask Bard...",command= bardGetAnswer)
        searchButton.grid(row=1, column=0, padx=20, pady=10, sticky="w")

def bardGetAnswer():
    prompt = entry.get()
    bard_GetAnswer(prompt)

