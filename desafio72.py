cem = 1
cemr = 1
cinqr = 1
cinq = 1
vint = 1
vintr = 1
dez = 1
dezr = 1
cinco = 1
cincor = 1
dois = 1
doisr = 1
um = 1
while True:
    print('Caixa eletrônico 24H')
    n = int(input('\nQual valor vocÊ quer sacar? '))
    cem = n / 100
    cemr = n % 100
    if int(cem) == 1: 
            print(f'Total de {int(cem)} cédula de R$ 100')
    if int(cem) > 1:
            print(f'Total de {int(cem)} cédulas de R$ 100')
    if cemr > 0:
        cinq = cemr / 50 
        cinqr = cemr % 50
        if int(cinq) == 1: 
            print(f'Total de {int(cinq)} cédula de R$ 50')
        if int(cinq) > 1:
            print(f'Total de {int(cinq)} cédulas de R$ 50')
    if cinqr > 0:
        vint = cinqr / 20
        vintr = cinqr % 20
        if int(vint) == 1: 
            print(f'Total de {int(vint)} cédula de R$ 20')
        if int(vint) > 1:
            print(f'Total de {int(vint)} cédulas de R$ 20')
    if vintr > 0:
        dez = vintr / 10
        dezr = vintr % 10
        if int(dez) == 1: 
            print(f'Total de {int(dez)} cédula de R$ 10')
        if int(dez) > 1:
            print(f'Total de {int(dez)} cédulas de R$ 10')
    if dezr > 0:
        cinco = dezr / 5
        cincor = dezr % 5
        if int(cinco) == 1: 
            print(f'Total de {int(cinco)} cédula de R$ 5')
        if int(cinco) > 1:
            print(f'Total de {int(cinco)} cédulas de R$ 5')
    if cincor > 0:
        dois = cincor / 2
        doisr = cincor % 2
        if int(dois) == 1: 
            print(f'Total de {int(dois)} cédula de R$ 2')
        if int(dois) > 1:
            print(f'Total de {int(dois)} cédulas de R$ 2')
    if doisr > 0:
        um = doisr / 1
        if int(um) == 1: 
            print(f'Total de {int(um)} moeda de R$ 1')
        if int(um) > 1:
            print(f'Total de {int(um)} moedas de R$ 1')
    break
