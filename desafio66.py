n = 0
med = 0
cont = 0
conti = ''
soma = 0
mai = 0
men = 0
while conti != 'N':
    n = int(input('Digite um número \n '))
    if cont == 0:
        mai = n
    elif mai < n:
        mai = n
    if cont == 0:
        men = n
    elif men > n:
        men = n
    soma = soma + n
    cont = cont + 1
    med = soma / cont
    conti = str(input('Digite [S] para continuar e [N] para parar. \n ')).upper().strip()
print('A média foi de {}. O maior valor lido foi {} e o menor valor foi {}'.format(med, mai, men))