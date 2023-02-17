n1 = int(input('Digite um número '))
while n1 < 0:
    n1 = int(input('Digite um número inteiro por favor'))
n2 = int(input('Digite outro número '))
while n2 < 0:
    n2 = int(input('Digite um número inteiro por favor'))
n3 = int(input('Digite outro número '))
while n3 < 0:
    n3 = int(input('Digite um número inteiro por favor'))
n4 = int(input('Digite outro número '))
while n4 < 0:
    n4 = int(input('Digite um número inteiro por favor'))
numeros = (n1, n2, n3, n4)
count = numeros.count(9)
ind = 9
litp = []
for c in numeros:
    if c % 2 == 0:
        litp.append(c)
for i in range(0, len(numeros)):
    if numeros[i] == 3 and ind == 9:
        ind = (i)
    #era só usar numeros.index(3)
print(litp)
print(f'O número 9 apareceu {count} vez(es).')
if ind != 9:
    print(f'O número 3 apareceu na {ind+1}ª posição na primeira vez.')
else:
    print('O número 3 não apareceu na tupla.')
if len(litp) > 0:
    print('Os números pares foram: {}'.format(str(litp)[1:-1]))
if len(litp) == 0:
    print('Não tem números pares no tuple.')
