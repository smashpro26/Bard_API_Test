import bardapi as Bard

token = "aghvyYEtYc7tIEMHmBx5Tkyjeo7DNjg9V0SYqWZlmq_gtBiPrPHVKnbMx7pnCaDP98hUNA."
bard = Bard(token=token)
answer = bard.get_answer("Green chutney vs red chutney?")['content']
print(answer)