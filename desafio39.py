n1 = int(input('Digite um número inteiro '))
n2 = int(input('Digite outro número inteiro '))

if n1 > n2:
    print('O primiro valor {} é maior que o segundo valor {}.'.format(n1,n2))
elif n2 > n1:
    print('O número segundo valor {} é maior que o primeiro valor {}.'.format(n2,n1))
elif n2 == n1:
    print('Os números tem o mesmo valor.')