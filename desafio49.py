s = 0
cont = 0
for c in range (1,501,2):
    if c%3==0:
        s = s + c
        cont = cont +1
print('A soma de todos os {} números impares entre 1 e 500 diviziveis por 3, tem como resultado:\n{}'.format(cont, s))
