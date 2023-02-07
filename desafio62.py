n1 = float(input('Digite o primeiro termo de sua PA '))
r = float(input('Digite a razão de sua PA '))
cont = 2
print('Os termos de sua PA são: \n{:.1f}'.format(n1), end = ' ')
while cont <= 10:
    pa = n1 + ((cont-1)*r)
    print('{:.1f}'.format(pa), end = ' ')
    cont = cont + 1
