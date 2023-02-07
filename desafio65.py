n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite números inteiros para soma-los, quando quiser terminar digite 999 \n'))
    soma = (soma + n)
    cont = cont + 1
print('A soma total do que você digitou foi {} e você digitou {} números?'.format(soma - 999, cont-1))