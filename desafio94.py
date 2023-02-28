a = {}
a["nome"] = str(input('Nome do jogador: ')).capitalize()
n = int(input(f'Quantas partidas {a["nome"]} jogou? '))
cont = 1
soma = 0
a["gols"] = list()
for b in range(0, n):
    g = int(input(f'Quantos gols na partida {cont}? '))
    soma = soma + g
    a["gols"].append(g)
    cont = cont + 1
a["soma"] = soma
print('-'*50)
print(a)
print('-'*50)
print(f'O nome do jogador é {a["nome"]}')
print(f'A quantidade de gols por partida foi: {a["gols"]}')
print(f'O total de gols de {a["nome"]} foi de {a["soma"]}')
print('-'*50)
print(f'O jogador {a["nome"]} jogou {n} partidas')
cont = 1
for c in range(0, len(a["gols"])):
    print(f'Na partida {cont}, fez {a["gols"][c]} gols.')
    cont = cont +1
print(f'Foi um total de {a["soma"]} gols.')
print('-'*50)