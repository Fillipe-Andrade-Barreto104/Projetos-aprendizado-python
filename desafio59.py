import random
from time import sleep
un = int(input('A máquina vai chutar um número entre 0 e 10, tente acertar qual foi '))
r = random.randint(0,10)
cont = 1
while un != r:
    sleep(0.4)
    un = int(input('Tente novamente, até acertar '))
    cont = cont +1
sleep(1)
if r == un:
    print('Parabéns, você venceu! E foram necessárias {} tentativas para você acertar.'.format(cont))
