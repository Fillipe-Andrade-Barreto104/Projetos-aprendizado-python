s = 0
pb = ''
vmb = 0
pmil = []
cont = 1
while True:
    no = str(input('Nome do produto: ')).capitalize().strip()
    pr = float(input('Preço: '))
    while pr == '':
        pr = int(input('Por favor digite algum valor '))
    while no == ' ':
        se = str(input('Digite algum nome por favor ')).capitalize().strip()
    if cont == 1:
        pb = no
        vmb = pr
    if pr < vmb:
        vmb = pr 
        pb = no
    if pr > 1000:
        pmil.append(pr)
    s = s + pr
    cont = cont + 1
    conti = str(input('Você gostaria de continuar? [S] para Sim e [N] para não. ')).capitalize().strip()[0]
    while conti != 'S' and conti != 'N':
        conti = str(input('Por favor digite S ou N ')).capitalize().strip()[0]
    if conti == 'N':
        break
print(f'Ao fim, o gasto total foi de R$ {s:.2f}, foram cadastrado(s) {len(pmil)} produto(s) com custo acima de R$ 1000.00. Por fim o nome do produto mais barato é {pb}, que custou  R$ {vmb:.2f}.')