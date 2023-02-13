mult = 1
cont = 1
while True:
    if cont == 1:
        n = float(input('Digite um número apra saber sua tabuada, quando quiser parar digite um número negativo. '))
    if n < 0:
        break
    mult = cont * n
    if cont == 1:
        print(f'\nA tabuada de {n:.2f} é: ')
    print(f'\n{n:.2f} * {cont:.0f} = {mult:.2f}')
    cont  = cont + 1
    if cont > 10:
        cont = 1
print('Fim')
    

