l = []
while True:
    n = int(input('Digite um valor '))
    l.append(n)
    esc = str(input('Quer continuar? [S] para sim e [N] para não ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor digite [S] ou [N] ')).upper()[0]
    if esc == 'N':
        break 
if len(l) > 1 :
    print(f'Foram digitados {len(l)} numeros')
else:
    print(f'Foram digitados {len(l)} numero')
print(f'A lista de valores em ordem decrescente é: {sorted(l,reverse=True)}')
if 5 in l:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
