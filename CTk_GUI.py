import customtkinter
from bard_AI import bard_GetAnswer

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global entry

        def bardGetAnswer():
            prompt = entry.get()
            answer = bard_GetAnswer(prompt)
            label.configure(text = answer['content'])
    

        self.grid_columnconfigure(0, weight=1)
        self.geometry("1000x600")
        self.title("Veg biriyani ahh")
        entry = customtkinter.CTkEntry(self, placeholder_text="Enter your prompt")
        entry.grid(row=0, column= 0, padx=20,pady=20,sticky = "ew", columnspan=2)

        searchButton = customtkinter.CTkButton(self, text= "Ask Bard...",command=bardGetAnswer)
        searchButton.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        myframe = customtkinter.CTkFrame(master=self)
        myframe.grid(row=2, column=0, padx=20, pady=20, sticky="nsew", columnspan = 4)

        label = customtkinter.CTkLabel(myframe, text="Placeholder",bg_color="transparent")
        label.grid(row=2, column=0, padx=20)
        label.configure(wraplength = 960)
        print(myframe.winfo_width())


        





