listao =[list() ,list()]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}o. valor: '))
    if n % 2 == 0:
        listao[0].append(n)
    else:
        listao[1].append(n)
print(f'Os valores pares digitados foram {sorted(listao[0])}')
print(f'Os valores ímpares digitados foram {sorted(listao[1])}')
