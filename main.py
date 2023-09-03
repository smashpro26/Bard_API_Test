import bardapi as Bard
#This comment was added from a the dev branch


token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)
#getting the answer from bard 
answer = bard.get_answer("Green chutney vs red chutney?")['content']
print(answer)
