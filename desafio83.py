l = []
lp = []
li = [] 
while True:
    n = int(input('Digite um valor '))
    l.append(n)
    esc = str(input('Quer continuar? [S] para sim e [N] para não ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor digite [S] ou [N] ')).upper()[0]
    if esc == 'N':
        break 
for v in range(0,len(l)):
    if l[v] %2 == 0:
        lp.append(l[v])
    if l[v] %2 != 0:
        li.append(l[v])
print(f'A lista com todos os números digitados é: {l}.')
print(f'A lista com somente os números pares é: {lp}.')
print(f'A lista com somentos os números ímpares digitados é:{li}')
