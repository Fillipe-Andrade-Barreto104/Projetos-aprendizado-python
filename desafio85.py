dados = []
pessoasp = list()
nomex = []
nomen = []
max = min = 0
cont = 0
while True: 
    dados.append(str(input('Digite seu nome ')).capitalize())
    dados.append(float(input('Digite seu peso em Kg ')))
    pessoasp.append(dados[:])
    dados.clear()
    esc = str(input('Quer continuar? [S] para sim e [N] para não ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor use S ou N ')).upper()[0]        
    if esc == 'N':
        break
for p in range(0, len(pessoasp)):
    if p == 0:
        max = min = pessoasp[p][1]
        nomex.append(pessoasp[p][0])
        nomen.append(pessoasp[p][0])
    else:
        if pessoasp[p][1] > max:
            nomex.clear()
            max = pessoasp[p][1]
            nomex.append(pessoasp[p][0])
        if pessoasp[p][1] == max and pessoasp[p][0] not in nomex:
            nomex.append(pessoasp[p][0])
        if pessoasp[p][1] < min:
            nomen.clear()
            min = pessoasp[p][1]
            nomen.append(pessoasp[p][0])
        if pessoasp[p][1] == min and pessoasp[p][0] not in nomen:
            nomen.append(pessoasp[p][0])
    cont = cont + 1
print(f'O total de pessoas cadastradas foram: {cont}')
print(f'O menor peso registrado foi {min} e a(s) pessoa(s) com tal peso foram: ',end='')
for c in range(0, len(nomen)):
    print(f'{nomen[c]}...', end = '')
print(f'\nO maior peso registrado foi {max} e a(s) pessoa(s) com tal peso foram: ',end='')
for i in range(0, len(nomex)):
    print(f'{nomex[i]}...', end = '')
print('')
