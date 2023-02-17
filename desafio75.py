from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
menor = numeros[0]
maior = numeros[0]
for c in numeros:
    if c < menor:
        menor = c
    if maior < c:
        maior = c
print(f'Os valores sorteados foram: {numeros}')
print(f'O menor valor foi: {menor}')
print(f'O maior valor sorteado foi: {maior}')
