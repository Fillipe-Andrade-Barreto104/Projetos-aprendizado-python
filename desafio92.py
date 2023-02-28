from random import randint
from time import sleep
lista = []
lista2 = []
aba = {}
cont = 1
for a in range(0,4):
    aba["jogador"] = str(input('Nome: ')).capitalize()
    aba["dado"] = randint(1,6)
    lista.append(aba.copy())
    print(f' {aba["jogador"]} tirou {aba["dado"]}')
sort = sorted(lista, key= lambda x:x['dado'], reverse=True) 
for c in range(0, len(sort)):
    print('-'*30)
    print(f'{cont}º lugar: {sort[c]["jogador"]} com {sort[c]["dado"]}')
    cont = cont+1
    print('-'*30)
    sleep(1)
