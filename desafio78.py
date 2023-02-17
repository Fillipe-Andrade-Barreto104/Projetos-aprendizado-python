palavra = ('alterar', 'animais', 'escurecer', 'cobra', 'janeiro', 'juntos', 'chaleira', 'lavanda', 'profissao', 'homem', 'estrangeiro', 'corte')
contp = 1
pala = 'a'
contl = 1
vogal = ''
for p in range(0,len(palavra)):
    print(f'Na palavra {palavra[p].upper()} temos as vogais: ', end = '')
    pala = [*palavra[p].upper()]
    for l in range(0,len(pala)):
        if pala[l] == 'A' or pala[l] == 'E' or pala[l] == 'I' or pala[l] == 'O' or pala[l] == 'U':
            print('{}'.format(pala[l].lower()), end = ' ')
    print('')
    

