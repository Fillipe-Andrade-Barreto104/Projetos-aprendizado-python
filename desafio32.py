di = float(input('Qual a distância da sua viagem em Km? '))
if di <= 200:
    v1 = di*0.5
    print('O valor da sua viagem vai ser: {:.2f}.'.format(v1))
else:
    v2 = di*0.45
    print('O valor da sua passgem vai ser: {:.2f}.'.format(v2))