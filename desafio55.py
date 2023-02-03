ln = []
li = []
contma = 0
contme = 0 
for c in range(1,8):
    print('----- {} PESSOA -----'.format(c))
    ln.append(str(input('Qual seu nome? ')).capitalize().strip())
    li.append(int(input('Qual sua idade? ')))
jun = list((zip(ln,li)))
for nome, idade in jun:
    if  idade >= 21:
        print('{} é maior de idade, pois tem {} anos(s).'.format(nome, idade))
        contma = contma + 1
    else:
        print('{} é menor de idade pois tem {} anos(s).'.format(nome, idade))
        contme = contme + 1
print('Ao todo temos {} menor(es) de idade e {} maior(es) de idade.'.format(contme, contma))
