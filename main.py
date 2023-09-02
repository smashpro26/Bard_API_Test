from bardapi import Bard
import os




token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)
answer = bard.get_answer("who is jordinidian??")['content']
print(answer)