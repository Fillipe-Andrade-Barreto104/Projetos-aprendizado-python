def ficha(n = '<desconhecido>', g = 0):
    return f'O jogador {n} fez {g} gols(s) no campeonato'
    


no = str(input('Nome do jogador: ').capitalize())
go = (input('Número de gols: '))

if go.isnumeric():
    go = int(go)
else:
    go = 0
if no.strip() == '':
    print(ficha(g =go))
else:
    print(ficha(no,go))

