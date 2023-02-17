tabela = ('Lápis', 0.80, 'Caneta', 1.50, 'Placa de vídeo', 1500.00, 'Nobreak', 460.00, 'Borracha', 1.00, 'Teclado', 150.00)
cont0 = 0
cont1 = 1
contp = 1
print('-'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('-'*30)
for n in range(0, len(tabela)):
    if cont1 <= len(tabela):
        print('{}'.format(tabela[cont0]),end = '')
        while len(tabela[cont0]) + contp < 20:
            print('.',end = '')
            contp = contp + 1
        print('R$', end = '')
        print("{:.2f}".format(tabela[cont1]).rjust(8))
        #......R${}'.format(tabela[cont0],tabela[cont1]))
        contp = 1
        cont0 = cont0 + 2
        cont1 = cont1 + 2
print('-'*30)
