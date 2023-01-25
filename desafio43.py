r1 = int(input('digite o comprimento da primeira reta '))
r2 = int(input('Digite o comprimento da segunda reta '))
r3 = int(input('Digite o comprimento da terceira reta '))

if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1 and r2 == r3 ==r1:
    print('É possível formar um triângulo e ele será equilátero.')
elif (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1 and r2 != r3 and r2 != r1 and r3 != r1:
    print('É possivel formar um triângulo e ele será escaleno.')
elif (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1 and r2 == r1 or r1 == r3 or r3 == r2:
    print('É possivel formar um triângulo e ele será isóceles.')
else:
    print('Não é possível formar um triângulo.')
