sa =  float(input('Digite o valor de seu salário para calcularmos o aumento '))
if sa>1250:
    s1 = sa*1.1
    print('Com seu atual salário de {:.2f}, seu novo será de {:.2f}.'.format(sa,s1))
else:
    s2 = sa*1.15
    print('Com seu atual salário de {:.2f}, seu novo será de {:.2f}.'.format(sa,s2)) 