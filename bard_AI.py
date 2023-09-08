from bardapi import Bard
import os

#token = os.environ.get('BARD_API_KEY')

token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)



def bard_GetAnswer(prompt):
    answer = bard.get_answer(prompt)
    print(answer['content'])
    