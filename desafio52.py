n1 = float(input('Qual o primeiro termo de sua PA? '))
r = float(input('Qual a razão de sua PA? '))
print('\nOs termos de sua PA são: \n{:.0f}'.format(n1))
for c in range(2,11):
    pa = n1 + ((c-1)*r)
    print('{:.0f}'.format(pa))
