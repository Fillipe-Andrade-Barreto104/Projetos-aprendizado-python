s =0
cont = 0
for c in range(0, 6):
    a = int(input('Digite números inteiros para somarmos '))
    if a%2 == 0:
        s = s + a
        cont = cont +1
print('A soma dos {} números pares fornecidos são: {}.'.format(cont, s))
