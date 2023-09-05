
#importing the bard api package
from bardapi import Bard
#importing the customtkinter package
import customtkinter
token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)
#getting the answer from bard 
answer = bard.get_answer("Green chutney vs red chutney?")['content']
print(answer)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("Veg biriyani ahh")
app = App()
app.mainloop()