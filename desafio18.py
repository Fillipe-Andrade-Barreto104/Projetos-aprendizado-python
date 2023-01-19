from math import sqrt
c1= float(input('Digite o valor dos catetos, para se achar a hipotenusa '))
c2= float(input(''))
h= sqrt((pow(c1,2)+pow(c2,2)))
print('A hipotenusa, dados os catetos {} e {}, tem o valor de {:.2f}'.format(c1,c2,h))
