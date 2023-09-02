from bardapi import Bard
import os




token = "aghvyYEtYc7tIEMHmBx5Tkyjeo7DNjg9V0SYqWZlmq_gtBiPrPHVKnbMx7pnCaDP98hUNA."
bard = Bard(token=token)
answer = bard.get_answer("who is jordinidian??")['content']
print(answer)