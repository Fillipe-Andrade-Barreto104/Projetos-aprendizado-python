from random import randint
from time import sleep
l = list()
def sorteio(lista):
    c = 0
    print('Sorteando 5 valores da lista: ', end = '')
    while c <= 4:
        a = randint(1,10)
        print(f'{a}', end= ' ', flush = True)
        sleep(0.5)
        lista.append(a)
        c += 1
    print('PRONTO!')

def somaPar(lista):
    sp = 0
    for a in range(0, len(lista)):
        if lista[a] % 2 == 0:
            sp += lista[a]
    print(f'Somando os valores pares de {lista}, temos {sp}')

sorteio(l)
somaPar(l)
