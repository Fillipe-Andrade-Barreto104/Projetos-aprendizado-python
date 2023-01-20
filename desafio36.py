r1 = int(input('digite o comprimento da primeira reta '))
r2 = int(input('Digite o comprimento da segunda reta '))
r3 = int(input('Digite o comprimento da terceira reta '))

if (r1+r2)>r3>abs(r2-r1):
    print('É possível formar um triângulo.')
elif (r1+r3)>r2>abs(r1-r3):
    print('É possível formar um triângulo.')
elif (r2+r3)>r1>abs(r2-r3):
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')