from bardapi import Bard

token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)



def bard_GetAnswer(prompt):
    answer = bard.get_answer(prompt)
    print(answer['content'])
    