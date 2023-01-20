import random
r = random.randint(0,5)
un = int(input('A máquina vai chutar um número entre 0 e 5, tente acertar qual foi '))
if r == un:
    print('Parabéns, você venceu!')
else:
    print('Que pena vocÊ perdeu.')