h = []
mai = []
mvin = []
while True:
    id = int(input('Idade: '))
    se = str(input('Sexo [M/F]: ')).capitalize().strip()
    while id == '':
        id = int(input('Por favor digite algum valor '))
    while se != 'M' and se != 'F':
        se = str(input('Digite ou M ou F ')).capitalize().strip()
    if id > 18:
        mai.append(id)
    if se == 'M': 
        h.append(se)
    if se == 'F' and id < 20:
        mvin.append(id)
    cont = str(input('Você gostaria de continuar? [S] para Sim e [N] para não. ')).capitalize().strip()
    while cont != 'S' and cont != 'N':
        cont = str(input('Por favor digite S ou N ')).capitalize().strip()
    if cont == 'N':
        break
print(f'Ao fim foram cadastradas {len(mai)} pessoa(s) com mais de 18 anos, {len(h)} homem(ns) e {len(mvin)} mulher(es) com menos de 20 anos.')
