media = 0
hmvi = 0
hmv = ''
lmn = []
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = (str(input('Digite seu nome ')).capitalize().strip())
    idade = (int(input('Digite sua idade ')))
    sexo = (str(input('Digite seu sexo: (F) de feminino ou (M) de masculino ')).capitalize().strip())
    media = media + idade
    if sexo == 'M' and  c == 1:
        hmvi = idade
        hmv = nome
    if sexo == 'M' and c > 1 and idade > hmvi:
        hmvi = idade
        hmv = nome
    if sexo == 'F' and idade < 20:
        lmn.append(nome)
media = media / 4
print('A média das idades é {}, o homem mais velho é {}. E a quantidade de mulheres abixo dos 20 anos de idade é {}.'.format(media, hmv, len(lmn)))

        
