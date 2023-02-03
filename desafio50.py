a = float(input('Digite um número para ver sua tabuada '))
print('\nA tabuada de {} é: \n'.format(a))
print('\033[31m-:-\033[m'*7)
for c in range(1, 21):
    tab = a * c
    print('\033[32m{} * {} = {}\033[m'.format(a,c,tab))
    print('\033[31m-:-\033[m'*7)
