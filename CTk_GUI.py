import customtkinter
from bard_AI import bard_GetAnswer


customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global entry
        self.geometry("1000x600")
        self.title("Veg biriyani ahh")
        entry = customtkinter.CTkEntry(self, placeholder_text="Enter your prompt")
        entry.pack()

        searchButton = customtkinter.CTkButton(self, text= "Ask Bard...",command= bardGetAnswer)
        searchButton.pack()

def bardGetAnswer():
    prompt = entry.get()
    bard_GetAnswer(prompt)

