map = 0
mep = 0
nmap = ''
nmep = ''
for c in range(1,4):
    print('----- {}ª PESSOA -----'.format(c))
    nome = (str(input('Digite seu nome ')).capitalize().strip())
    peso = (float(input('Digite seu peso em Kg ')))
    if c == 1:
        map = peso
        nmap = nome
    if c > 1 and  map < peso:
        map = peso
        nmap = nome
    if c == 1:
        mep = peso
        nmep = nome
    if c > 1 and mep > peso:
        mep = peso
        nmep = nome
print('{} é quem tem mais peso pois tem {}, e aquele(a) é o(a) leve tem {}, e seu nome é {}.'.format(nmap, map, mep, nmep))
