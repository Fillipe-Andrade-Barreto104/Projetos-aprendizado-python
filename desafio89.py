from random import randint
from time import sleep
listao = list()
print('-'*30)
print('JOGO NA MEGA SENA'.center(30))
print('-'*30)
n = int(input('Quantos jogos da Mega Sena você vai jogar. '))
cont = 1
rand = 0
print('-'*30)
print(f'Sorteando {n} jogos'.upper().center(30))
print('-'*30)
for c in range(0, n):
    listao.append(list())
    while cont <=6:
        rand = randint(0, 60)
        while rand in listao[c]:
            rand = randint(0, 60)
        if rand not in listao[c]:
            listao[c].append(rand)
        cont = cont +1
    cont = 1
    print(f'Jogo {c+1}: {sorted(listao[c])}')
    sleep(1)    
print('-'*30)
print('BOA SORTE'.center(30))
print('-'*30)

