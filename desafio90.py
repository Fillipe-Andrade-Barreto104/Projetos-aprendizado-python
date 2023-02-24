from time import sleep
lista = []
cont = 0
cont2 = 0
a = []
while True:
    lista.append(list())
    lista[cont].append((str(input('Nome: ').capitalize())))
    a.append(float(input('Nota 1: ')))
    a.append(float(input('Nota 2: ')))
    media = (a[0]+a[1])/2
    a.append(media)
    lista[cont].append(list(a[:]))

    esc = str(input('Digite [S] para continuar e [N] para parar. ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor digite [S] ou [N] ')).upper()[0]
    if esc == 'N':
        break
    cont = cont + 1
    a.clear()
print('No.', end = '')
print(' NOME', end = '')
print('MÉDIA'.rjust(15))
print('-'*25)
for c in range(0, len(lista)):
    print(f'{c}', end= '  ')
    print(f'{lista[c][0]}', end = '')
    if len(lista[c][0]) > 0:
        n = 20 - len(lista[c][0])
        print(f'{lista[c][1][2]:.2f}'.rjust(n))
    cont2 = cont2 +1
while True:
    print('-'*40)
    n = int(input(f'Mostrar as notas de qual aluno? ({len(lista)} interrompe): '))
    if n > (len(lista)-1):
        break
    print(f'As notas de {lista[n][0]} são {lista[n][1][:2]}')
    print('-'*40)
print('Finalizando...'.upper())
sleep(1)
print('<<< volte sempre >>>'.upper())