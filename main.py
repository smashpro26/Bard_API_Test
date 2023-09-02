import bardapi as Bard

token = "aghvyV3AkqdVIl_a4Qmwsf844o8-l_zCIh8qVXiuBsVoU_1KeajaTGqEmc2FOtTaLn_6-A."
bard = Bard(token=token)
#getting the answer from bard k;askf a dlaKJSDhlk hello world
answer = bard.get_answer("Green chutney vs red chutney?")['content']
print(answer)
