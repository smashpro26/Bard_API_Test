from bardapi import Bard

token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)

def bardGetAnswer(prompt):
    answer = bard.get_answer("What is tkinter")
    print(answer['content'])