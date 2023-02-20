numeros = []
esc = 'A'
while True:
    n = int(input('Digite um número inteiro '))
    if n in numeros:
        print('Esse número já está na lista')
        esc = str(input('Quer adicionar mais um número? [S/N] ')).upper()[0]
        while esc != 'N' and esc !='S':
           esc = str(input('Por favor digite algo dentro dos parâmetros? [S] para sim e [N] para não ')).upper()[0] 
        if esc == 'N':
            break
    if esc != 'S' and esc != 'N':
        esc = str(input('Quer adicionar mais um número? [S/N] ')).upper()[0]
    while esc != 'N' and esc !='S':
           esc = str(input('Por favor digite algo dentro dos parâmetros? [S] para sim e [N] para não ')).upper()[0] 
    if n  not in numeros:
        numeros.append(n)
    if esc == 'N':
        break
    esc = 'A'
if len(numeros)> 1:
    print('Ao fim os números colocados na lista foram: {}'.format(sorted(numeros)))
else:
    print(f'Ao fim o número colocado na lista foi: {numeros}')
